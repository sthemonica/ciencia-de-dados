# Aula 3 — Pandas e DataFrames

O Pandas é uma biblioteca muito usada para análise de dados. Se o NumPy é ótimo para trabalhar com números, o Pandas é ótimo para trabalhar com **tabelas**, que misturam textos, números e datas, com colunas nomeadas.

Ele não vem instalado com o Python, então precisamos instalar pelo terminal:

```bash
uv add pandas
```

O Pandas usa o NumPy por baixo dos panos, então muito do que vimos na aula anterior vai aparecer de novo aqui.

**Series e DataFrame**

O Pandas tem duas estruturas principais:

- **Series**: uma coluna de dados, com um índice (a numeração de cada linha)
- **DataFrame**: uma tabela, com linhas e colunas, parecida com uma planilha. Cada coluna de um DataFrame é uma Series

```python
# arquivo exemplo_series.py
import pandas as pd

temperaturas = pd.Series([18, 21, 19])
print(temperaturas)
```

O resultado será:

```text
0    18
1    21
2    19
dtype: int64
```

Repare que, diferente do array do NumPy, a Series mostra o índice (0, 1, 2) ao lado de cada valor.

O `as pd` é um apelido. Por convenção, toda a comunidade chama o Pandas de `pd`, então escrevemos `pd.Series` em vez de `pandas.Series`.

**Lendo um arquivo**

Na prática, quase sempre criamos um DataFrame lendo um arquivo. Vamos usar o arquivo `pessoas.csv`:

```text
nome,idade,cidade
Ana,28,Curitiba
Bruno,35,Ponta Grossa
Carla,22,Londrina
Diego,41,Curitiba
Elisa,30,Ponta Grossa
```

```python
# arquivo ler_pandas.py
import pandas as pd

tabela = pd.read_csv("pessoas.csv")
print(tabela)
```

O resultado será:

```text
    nome  idade        cidade
0    Ana     28      Curitiba
1  Bruno     35  Ponta Grossa
2  Carla     22      Londrina
3  Diego     41      Curitiba
4  Elisa     30  Ponta Grossa
```

**Conhecendo os dados**

Quando abrimos uma tabela nova, o primeiro passo é entender o que tem nela:

```python
print(tabela.head(2))
print(tabela.shape)
print(tabela.describe())
```

- `head(2)`: mostra as 2 primeiras linhas. Sem o número, mostra 5. Muito útil para tabelas grandes
- `shape`: formato da tabela, igual ao do NumPy. No caso, `(5, 3)`: 5 linhas e 3 colunas
- `describe()`: um resumo estatístico das colunas numéricas

O resultado do `describe()` será:

```text
           idade
count   5.000000
mean   31.200000
std     7.190271
min    22.000000
25%    28.000000
50%    30.000000
75%    35.000000
max    41.000000
```

Em uma linha, temos quantidade, média, desvio padrão, mínimo, máximo e os quartis (`50%` é a mediana).

**Selecionando colunas**

Para pegar uma coluna, usamos o nome dela entre colchetes, parecido com um dicionário:

```python
print(tabela["idade"])
print(tabela["idade"].mean())
```

A coluna `idade` é uma Series, e por isso tem as mesmas funções de estatística do array: `mean`, `max`, `min`, `sum`. O resultado da média será `31.2`.

Para pegar mais de uma coluna, passamos uma **lista** de nomes (por isso os colchetes duplos):

```python
print(tabela[["nome", "cidade"]])
```

**Selecionando linhas**

Para acessar linhas, usamos o `loc` (pelo índice) ou o `iloc` (pela posição):

```python
print(tabela.loc[1])
print(tabela.loc[1, "nome"])
print(tabela.iloc[0, 0])
```

- `tabela.loc[1]`: a linha de índice 1, ou seja, os dados do Bruno
- `tabela.loc[1, "nome"]`: a linha 1, coluna `nome`, que é `Bruno`
- `tabela.iloc[0, 0]`: a primeira linha e a primeira coluna pela posição, que é `Ana`

Por enquanto, a diferença entre os dois é pequena. Ela aparece quando filtramos ou ordenamos a tabela, porque o índice de cada linha continua o mesmo, mas a posição muda.

**Filtrando dados**

Lembra do filtro com condições do NumPy? No Pandas funciona do mesmo jeito:

```python
maiores_de_25 = tabela[tabela["idade"] > 25]
print(maiores_de_25)
```

O resultado será:

```text
    nome  idade        cidade
0    Ana     28      Curitiba
1  Bruno     35  Ponta Grossa
3  Diego     41      Curitiba
4  Elisa     30  Ponta Grossa
```

Repare que a Carla (índice 2) sumiu, mas os índices das outras pessoas continuam os mesmos.

Para combinar condições, usamos `&` (e) e `|` (ou), com cada condição entre parênteses:

```python
filtro = tabela[(tabela["idade"] > 25) & (tabela["cidade"] == "Curitiba")]
print(filtro)
```

O resultado será apenas Ana e Diego.

> Atenção: aqui não usamos `and` e `or` como nas condicionais. No Pandas e no NumPy, usamos `&` e `|`, e os parênteses são obrigatórios.

**Ordenando**

```python
print(tabela.sort_values("idade", ascending=False))
```

O `sort_values` ordena pela coluna informada. O `ascending=False` deixa em ordem decrescente, da pessoa mais velha para a mais nova.

**Criando colunas e salvando**

```python
tabela["idade_em_10_anos"] = tabela["idade"] + 10
tabela.to_csv("pessoas_atualizado.csv", index=False)
```

Aqui, criamos uma nova coluna calculada a partir da idade, somando 10 em todas as linhas de uma vez, sem `for`, igual ao NumPy. Depois, salvamos o resultado em um novo arquivo com o `to_csv`.

O `index=False` evita que o Pandas salve a numeração das linhas (0, 1, 2...) como uma coluna extra no arquivo.

**Agrupando e contando**

Uma das perguntas mais comuns em análise de dados é "qual o valor por grupo?". Para isso usamos o `groupby`:

```python
print(tabela.groupby("cidade")["idade"].mean())
```

O resultado será:

```text
cidade
Curitiba        34.5
Londrina        22.0
Ponta Grossa    32.5
Name: idade, dtype: float64
```

Lemos assim: agrupe as linhas por `cidade`, pegue a coluna `idade` e calcule a média de cada grupo.

Para contar quantas vezes cada valor aparece, usamos o `value_counts`:

```python
print(tabela["cidade"].value_counts())
```

O resultado será:

```text
cidade
Curitiba        2
Ponta Grossa    2
Londrina        1
Name: count, dtype: int64
```

**Outros formatos**

O Pandas também lê outros formatos:

```python
tabela = pd.read_csv("pessoas.csv", sep=";")
tabela = pd.read_json("pessoas.json")
tabela = pd.read_excel("pessoas.xlsx")
```

O `sep=";"` serve para CSVs separados por ponto e vírgula. O `read_json` funciona bem quando o JSON é uma lista de registros, como uma lista de pessoas. Para ler arquivos do Excel, pode ser preciso instalar também o pacote `openpyxl` com `uv add openpyxl`.

**Qual usar?**

- Para arquivos pequenos e tarefas simples, como ler uma configuração ou salvar alguns registros, os módulos `csv` e `json` resolvem bem e não precisam de instalação
- Para analisar, filtrar e transformar dados em formato de tabela, o Pandas economiza muito código
- O `txt` não tem estrutura, então pode ser lido com o `open` mesmo

E lembre do tópico de tratamento de erros: ao abrir um arquivo que pode não existir, vale envolver a leitura em um bloco `try` e `except`.

**Resumo**

- A Series é uma coluna, e o DataFrame é uma tabela formada por várias Series
- `head`, `shape` e `describe` ajudam a conhecer os dados
- `tabela["coluna"]` seleciona colunas, e `loc` e `iloc` selecionam linhas
- Filtros funcionam como no NumPy, usando `&` e `|` para combinar condições
- `sort_values` ordena, `groupby` agrupa e `value_counts` conta
