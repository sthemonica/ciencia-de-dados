# Capstone Fraude — Aula 1: Carregando os dados

Nesta aula vamos abrir os três arquivos do case, entender a estrutura de cada um e juntar tudo em uma única tabela.

Crie o notebook `notebooks/01_carregamento.ipynb`.

**Relembrando: Series e DataFrame**

Antes de abrir os arquivos, vamos criar um exemplo pequeno à mão para relembrar as duas estruturas do Pandas.

```python
import pandas as pd

valores = pd.Series([5.64, 124.71, 339.32], name="valor_compra")
print(valores)
```

O resultado será:

```text
0      5.64
1    124.71
2    339.32
Name: valor_compra, dtype: float64
```

A **Series** é uma coluna: valores com um índice (0, 1, 2) e um nome. Já o **DataFrame** é uma tabela, e podemos criar um a partir de um dicionário, onde cada chave vira uma coluna:

```python
exemplo = pd.DataFrame({
    "pais": ["BR", "BR", "AR"],
    "valor_compra": [5.64, 124.71, 339.32],
    "fraude": [0, 0, 1],
})
print(exemplo)
```

O resultado será:

```text
  pais  valor_compra  fraude
0   BR          5.64       0
1   BR        124.71       0
2   AR        339.32       1
```

Para entender a estrutura de um DataFrame, usamos:

- `exemplo.shape`: formato da tabela, no caso `(3, 3)`
- `exemplo.columns`: os nomes das colunas
- `exemplo.dtypes`: o tipo de cada coluna (`str` para texto, `float64` para decimais, `int64` para inteiros)

Cada coluna do DataFrame, como `exemplo["pais"]`, é uma Series.

**Carregando o Excel**

```python
marco = pd.read_excel("../data/raw/compras_marco.xlsx")
print(marco.shape)
marco.head()
```

O resultado do `shape` será `(76961, 18)`: quase 77 mil compras e 18 colunas.

O `../` no caminho significa "voltar uma pasta". O notebook está dentro de `notebooks`, então precisamos voltar para a pasta do projeto e depois entrar em `data/raw`.

O `read_excel` só funciona porque instalamos o `openpyxl` na aula anterior.

**Carregando o CSV**

O CSV de abril foi exportado no padrão brasileiro: colunas separadas por `;` e decimais com vírgula (`2,69` em vez de `2.69`). Se abrirmos sem avisar o Pandas, tudo fica em uma única coluna. Por isso usamos dois parâmetros:

```python
abril = pd.read_csv("../data/raw/compras_abril.csv", sep=";", decimal=",")
print(abril.shape)
```

O resultado será `(73289, 18)`.

- `sep=";"`: indica o separador das colunas
- `decimal=","`: indica que a vírgula é o separador decimal

Repare em uma diferença importante entre as duas tabelas:

```python
print(marco["data_compra"].dtype)
print(abril["data_compra"].dtype)
```

O resultado será:

```text
datetime64[us]
str
```

O Excel guarda datas como datas, mas o CSV é só texto. Vamos corrigir isso na aula de limpeza.

**Carregando o JSON**

```python
documentos = pd.read_json("../data/raw/documentos.json")
print(documentos.shape)
documentos.head()
```

O resultado será:

```text
   idCompra  doc1 doc2 doc3
0         1     1  NaN    N
1         2     1    Y    N
2         3     1  NaN    N
3         4     1  NaN    Y
4         5     1  NaN    N
```

O arquivo é uma lista de registros, um por compra, então o `read_json` monta a tabela direto. O `NaN` indica um valor ausente.

**Renomeando colunas**

O sistema de documentos usa nomes diferentes dos nossos: `idCompra` em vez de `id_compra`. Vamos padronizar com o `rename`, passando um dicionário com o nome antigo e o novo:

```python
documentos = documentos.rename(columns={
    "idCompra": "id_compra",
    "doc1": "entrega_doc_1",
    "doc2": "entrega_doc_2",
    "doc3": "entrega_doc_3",
})
```

O `rename` não altera a tabela original: ele devolve uma nova, por isso guardamos o resultado de volta na variável `documentos`.

**Empilhando tabelas com `concat`**

Março e abril têm as mesmas colunas, então podemos empilhar uma embaixo da outra:

```python
compras = pd.concat([marco, abril], ignore_index=True)
print(len(marco), "+", len(abril), "=", len(compras))
```

O resultado será `76961 + 73289 = 150250`.

O `ignore_index=True` cria uma numeração nova para as linhas. Sem ele, os índices se repetiriam, porque as duas tabelas começam do 0.

**Juntando tabelas com `merge`**

Agora queremos colocar as colunas de documentos **ao lado** das compras. Para isso, usamos o `merge`, que junta as tabelas usando uma coluna em comum, a `id_compra`:

```python
dados = compras.merge(documentos, on="id_compra", how="left")
print(dados.shape)
```

O resultado será `(150250, 21)`: as 18 colunas das compras mais as 3 de documentos.

O `how` define o que fazer quando uma compra não aparece nas duas tabelas:

- `"left"`: mantém todas as linhas da tabela da esquerda (`compras`)
- `"inner"`: mantém só as linhas que existem nas duas
- `"outer"`: mantém todas as linhas das duas tabelas

> A diferença entre `concat` e `merge`: o `concat` empilha tabelas com as **mesmas colunas**, e o `merge` junta tabelas com **colunas diferentes**, usando uma chave em comum.

Será que o `merge` deixou alguma compra sem documentos?

```python
dados[["entrega_doc_1", "entrega_doc_2", "entrega_doc_3"]].isna().sum()
```

O resultado será:

```text
entrega_doc_1         0
entrega_doc_2    109038
entrega_doc_3         0
```

Como `entrega_doc_1` e `entrega_doc_3` não têm ausentes, todas as compras encontraram seu registro de documentos. Os ausentes de `entrega_doc_2` já vieram assim do sistema, e vamos tratar na limpeza.

Repare também que juntamos 76.961 + 73.289 = 150.250 compras, mas a empresa disse que eram 150 mil. Guarde essa pista para a próxima aula!

**Salvando a base unificada**

```python
dados.to_csv("../data/processed/compras_unificado.csv", index=False)
```

Na próxima aula, o notebook de limpeza vai começar lendo esse arquivo.

**Salvando no GitHub**

```bash
git add .
git commit -m "Adiciona carregamento e unificação dos dados"
git push
```

**Resumo**

- `pd.Series` e `pd.DataFrame` criam as estruturas à mão, e `shape`, `columns` e `dtypes` mostram a estrutura
- `read_excel`, `read_csv` e `read_json` carregam cada formato
- No CSV, `sep` e `decimal` resolvem o padrão brasileiro
- `rename` padroniza os nomes das colunas
- `concat` empilha tabelas, e `merge` junta tabelas lado a lado por uma chave
