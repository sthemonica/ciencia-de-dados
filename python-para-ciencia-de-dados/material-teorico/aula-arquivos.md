- Como criar e editar arquivos: txt, csv, json

Os arquivos são a forma de guardar informações que continuam existindo depois que o programa termina. Tudo que fica em variáveis some quando o programa é encerrado, já o que é salvo em um arquivo fica guardado no computador.

Os três formatos mais comuns para guardar dados em texto são o `.txt`, o `.csv` e o `.json`. Todos eles podem ser criados e editados em qualquer editor de texto, como o Bloco de Notas ou o VS Code: basta criar um arquivo novo e salvar com a extensão desejada.

**txt**

O `.txt` é o formato mais simples que existe: é só texto, sem nenhuma estrutura ou regra.

```text
Lista de compras
arroz
feijão
café
Lembrar de passar na padaria
```

Ele é bom para guardar anotações, logs (registros do que o programa fez) e qualquer texto livre. O problema é que, como não tem estrutura, o computador não sabe o que cada linha significa, ele só enxerga texto.

**csv**

O `.csv` (Comma-Separated Values, ou valores separados por vírgula) guarda dados em formato de **tabela**, como uma planilha do Excel.

```text
nome,idade,cidade
Ana,28,Curitiba
Bruno,35,Ponta Grossa
Carla,22,Londrina
```

Como ele funciona:
- Cada linha é uma linha da tabela
- Os valores de cada coluna são separados por vírgula
- A primeira linha geralmente é o **cabeçalho**, com o nome de cada coluna

Visualmente, o arquivo acima representa essa tabela:

| nome  | idade | cidade       |
|-------|-------|--------------|
| Ana   | 28    | Curitiba     |
| Bruno | 35    | Ponta Grossa |
| Carla | 22    | Londrina     |

Um detalhe: no Brasil, é comum encontrar CSVs separados por ponto e vírgula (`;`), porque a vírgula já é usada nos números decimais (`3,50`). Os dois formatos funcionam, só precisamos saber qual separador está sendo usado.

O CSV pode ser aberto direto no Excel ou no Google Planilhas, por isso é muito usado para exportar e importar dados entre sistemas.

**json**

O `.json` (JavaScript Object Notation) guarda dados de forma **organizada em chaves e valores**, muito parecido com os dicionários e listas do Python.

```json
{
    "nome": "Ana",
    "idade": 28,
    "ativa": true,
    "cursos": ["Python", "SQL"],
    "endereco": {
        "cidade": "Curitiba",
        "estado": "PR"
    }
}
```

Como ele funciona:
- As chaves `{ }` representam um objeto (no Python, um dicionário)
- Os colchetes `[ ]` representam uma lista
- Cada informação é um par `"chave": valor`
- As chaves (nomes) ficam sempre entre aspas duplas
- Os valores podem ser texto, número, `true`/`false`, `null`, listas ou outros objetos

A grande vantagem do JSON é que ele consegue guardar informações **dentro de informações**, como o endereço dentro da pessoa no exemplo acima. Isso seria difícil de representar em um CSV.

Por isso, o JSON é o formato mais usado para troca de dados na internet: quando um aplicativo busca informações de um servidor, geralmente elas chegam em JSON.

> Uma forma de pensar nos três formatos:
>
> O **txt** é um caderno em branco, você escreve do jeito que quiser.
>
> O **csv** é uma planilha, tudo organizado em linhas e colunas.
>
> O **json** é uma ficha de cadastro, com campos nomeados e que pode ter fichas dentro de fichas.

---

- Como ler esses tipos de arquivos no Python

Agora que sabemos como cada arquivo funciona, vamos ver como ler e editar eles pelo código.

**A função open**

Para trabalhar com qualquer arquivo no Python, usamos a função `open`, que recebe o nome do arquivo e o **modo** de abertura:

- `"r"`: leitura (read). É o modo padrão, e dá erro se o arquivo não existir
- `"w"`: escrita (write). Cria o arquivo, ou **apaga todo o conteúdo** se ele já existir
- `"a"`: adicionar (append). Escreve no final do arquivo, sem apagar o que já tem

```python
# arquivo abrir_arquivo.py
with open("anotacoes.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
```

O `with` abre o arquivo e **fecha automaticamente** quando o bloco termina. Sem ele, precisaríamos lembrar de chamar `arquivo.close()`, e um arquivo esquecido aberto pode causar problemas. Por isso, sempre use o `with`.

O `encoding="utf-8"` garante que acentos e caracteres especiais, como `ç` e `ã`, sejam lidos corretamente.

**Lendo txt**

```python
# arquivo ler_txt.py
with open("compras.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
```

O `read()` lê o arquivo inteiro de uma vez e guarda tudo em uma única variável de texto.

```python
with open("compras.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())
```

Também podemos percorrer o arquivo linha por linha com um `for`. O `strip()` remove a quebra de linha que fica no final de cada linha.

**Escrevendo txt**

```python
# arquivo escrever_txt.py
with open("compras.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("arroz\n")
    arquivo.write("feijão\n")
```

Com o modo `"w"`, o arquivo é criado do zero. Se ele já existia, todo o conteúdo anterior é apagado.

O `\n` representa uma quebra de linha. Sem ele, todos os itens ficariam grudados na mesma linha.

```python
with open("compras.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("café\n")
```

Com o modo `"a"`, o texto é adicionado no final do arquivo, mantendo o que já estava lá.

**Lendo csv**

O Python tem o módulo `csv` na biblioteca padrão, que já sabe lidar com as vírgulas e as colunas para nós.

```python
# arquivo ler_csv.py
import csv

with open("pessoas.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(f"{linha['nome']} tem {linha['idade']} anos")
```

O `DictReader` usa o cabeçalho para transformar cada linha em um dicionário, assim acessamos os valores pelo nome da coluna: `linha['nome']`.

Atenção: todos os valores lidos de um CSV chegam como **texto**. Se quisermos fazer contas com a idade, precisamos converter com `int(linha['idade'])`.

Se o CSV for separado por ponto e vírgula, basta informar: `csv.DictReader(arquivo, delimiter=";")`.

**Escrevendo csv**

```python
# arquivo escrever_csv.py
import csv

pessoas = [
    {"nome": "Ana", "idade": 28, "cidade": "Curitiba"},
    {"nome": "Bruno", "idade": 35, "cidade": "Ponta Grossa"},
]
```

Primeiro, montamos os dados que queremos salvar: uma lista de dicionários, onde cada dicionário é uma linha da tabela.

```python
with open("pessoas.csv", "w", encoding="utf-8", newline="") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=["nome", "idade", "cidade"])
    escritor.writeheader()
    escritor.writerows(pessoas)
```

- `fieldnames`: a lista com o nome das colunas
- `writeheader()`: escreve a linha do cabeçalho
- `writerows()`: escreve todas as linhas de uma vez

O `newline=""` evita que o Python crie linhas em branco extras entre os registros, algo que acontece principalmente no Windows.

**Lendo json**

Para o JSON, usamos o módulo `json`, também da biblioteca padrão. Ele converte o conteúdo do arquivo direto em dicionários e listas do Python.

```python
# arquivo ler_json.py
import json

with open("aluna.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
```

O `json.load` lê o arquivo e transforma o conteúdo em um dicionário do Python.

```python
print(dados["nome"])
print(dados["endereco"]["cidade"])
```

A partir daí, acessamos as informações como em qualquer dicionário. O resultado será `Ana` e `Curitiba`.

**Escrevendo json**

```python
# arquivo escrever_json.py
import json

aluna = {
    "nome": "Ana",
    "idade": 28,
    "cursos": ["Python", "SQL"]
}
```

```python
with open("aluna.json", "w", encoding="utf-8") as arquivo:
    json.dump(aluna, arquivo, indent=4, ensure_ascii=False)
```

- `json.dump`: pega um dicionário/lista do Python e salva no arquivo
- `indent=4`: deixa o arquivo organizado e legível, com 4 espaços de indentação
- `ensure_ascii=False`: mantém os acentos como estão, em vez de trocar por códigos estranhos como `\u00e7`

**Editando um arquivo existente**

Não existe um comando para "editar" um arquivo diretamente. O caminho é sempre o mesmo, em três passos:

1. Ler o arquivo para uma variável
2. Alterar a variável
3. Salvar a variável de volta no arquivo

```python
# arquivo editar_json.py
import json

with open("aluna.json", "r", encoding="utf-8") as arquivo:
    aluna = json.load(arquivo)
```

Primeiro, lemos o arquivo e guardamos o conteúdo na variável `aluna`.

```python
aluna["idade"] = 29
aluna["cursos"].append("Pandas")
```

Depois, alteramos a variável como faríamos com qualquer dicionário.

```python
with open("aluna.json", "w", encoding="utf-8") as arquivo:
    json.dump(aluna, arquivo, indent=4, ensure_ascii=False)
```

Por fim, salvamos a variável de volta no arquivo, substituindo o conteúdo antigo.

Esse mesmo raciocínio vale para o txt e o csv.