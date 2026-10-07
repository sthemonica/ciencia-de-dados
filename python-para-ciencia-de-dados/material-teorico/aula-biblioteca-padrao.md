# Aula 1 — Bibliotecas importantes: os, sys, datetime, re

Uma biblioteca (ou módulo) é um conjunto de códigos prontos, escritos por outras pessoas (ou nós mesmos!), que podemos usar no nosso programa sem precisar reinventar a roda.

O Python já vem com várias bibliotecas instaladas, a chamada **biblioteca padrão**. Para usar uma delas, basta importar no topo do arquivo com a palavra chave `import`:

```python
import os
import sys
```

> Pense nas bibliotecas como uma caixa de ferramentas. Você não precisa fabricar um martelo toda vez que quiser pregar um prego, basta pegar o martelo que já está na caixa.

Nesta aula vamos conhecer quatro módulos da biblioteca padrão. Nas próximas aulas, vamos ver bibliotecas que **não** vêm com o Python e precisam ser instaladas: NumPy, Pandas e Matplotlib.

**os**

O módulo `os` serve para conversar com o sistema operacional (Windows, Linux, macOS): navegar por pastas, listar arquivos, criar diretórios e verificar se um arquivo existe.

```python
# arquivo exemplo_os.py
import os

print(os.getcwd())
print(os.listdir())
```

- `os.getcwd()`: mostra a pasta onde o programa está rodando
- `os.listdir()`: lista os arquivos e pastas dessa pasta

```python
if not os.path.exists("relatorios"):
    os.mkdir("relatorios")
```

Aqui verificamos se a pasta `relatorios` existe com o `os.path.exists`. Se não existir, criamos ela com o `os.mkdir`.

```python
caminho = os.path.join("relatorios", "janeiro.txt")
print(caminho)
```

O resultado será `relatorios/janeiro.txt`.

O `os.path.join` monta o caminho do arquivo do jeito certo para cada sistema. No Windows, as pastas são separadas por `\`, e no Linux e macOS por `/`. Usando o `join`, o Python resolve isso para você.

**sys**

O módulo `sys` dá acesso a informações do próprio Python e da execução do programa.

```python
# arquivo exemplo_sys.py
import sys

print(sys.version)
print(sys.argv)
```

- `sys.version`: mostra a versão do Python instalada
- `sys.argv`: lista com o nome do arquivo e os valores digitados depois dele no terminal

Se rodarmos no terminal `python exemplo_sys.py Sthefanie`, o `sys.argv` será a lista `['exemplo_sys.py', 'Sthefanie']`.

```python
if len(sys.argv) < 2:
    print("Informe seu nome ao rodar o programa")
    sys.exit()

print(f"Olá, {sys.argv[1]}!")
```

Nesse código, se o usuário não informar o nome ao rodar o programa no terminal, mostramos um aviso e usamos o `sys.exit()` para encerrar a execução na hora.

Se o nome for informado, a mensagem `Olá, Sthefanie!` será mostrada.

**datetime**

O módulo `datetime` serve para trabalhar com datas e horas: pegar a data atual, formatar, somar dias e calcular diferenças.

```python
# arquivo exemplo_datetime.py
from datetime import datetime, timedelta

agora = datetime.now()
print(agora.strftime("%d/%m/%Y %H:%M"))
```

Repare que aqui usamos `from datetime import datetime, timedelta`. Essa forma importa só as partes que vamos usar, assim escrevemos `datetime.now()` em vez de `datetime.datetime.now()`.

O `datetime.now()` pega a data e hora atuais, e o `strftime` transforma essa data em texto, no formato que quisermos. O resultado será algo como `30/09/2026 20:57`.

Os códigos de formatação mais usados são:
- `%d`: dia
- `%m`: mês
- `%Y`: ano com 4 dígitos
- `%H`: hora
- `%M`: minuto

```python
daqui_uma_semana = agora + timedelta(days=7)
print(daqui_uma_semana.strftime("%d/%m/%Y"))
```

O `timedelta` representa um intervalo de tempo, que podemos somar ou subtrair de uma data.

```python
nascimento = datetime.strptime("15/03/1998", "%d/%m/%Y")
dias_vividos = (agora - nascimento).days
```

O `strptime` faz o contrário do `strftime`: transforma um texto em data. Depois, ao subtrair uma data da outra, conseguimos saber quantos dias se passaram entre elas.

**re**

O módulo `re` trabalha com **expressões regulares**, que são padrões usados para procurar, validar ou substituir trechos de texto.

```python
# arquivo exemplo_re.py
import re

texto = "Meu telefone é 42 99999-1234 e o do trabalho é 42 3222-5678"
telefones = re.findall(r"\d{4,5}-\d{4}", texto)
```

O `re.findall` encontra todos os trechos que combinam com o padrão. Nesse caso, a variável `telefones` será a lista `['99999-1234', '3222-5678']`.

```python
email = "sthefanie@email.com"

if re.search(r"^\S+@\S+\.\S+$", email):
    print("E-mail válido")
```

O `re.search` verifica se o padrão aparece no texto. Aqui, usamos ele para validar se o e-mail tem o formato `algo@algo.algo`.

```python
cpf = "123.456.789-00"
somente_numeros = re.sub(r"\D", "", cpf)
```

O `re.sub` substitui os trechos que combinam com o padrão. Aqui, trocamos tudo que não é número por nada, e o resultado será `12345678900`.

Alguns símbolos básicos dos padrões:
- `\d`: qualquer número
- `\D`: qualquer coisa que **não** seja número
- `\S`: qualquer caractere que não seja espaço
- `+`: uma ou mais vezes
- `{4,5}`: entre 4 e 5 vezes
- `^` e `$`: início e fim do texto

O `r` antes das aspas indica uma "raw string", que faz o Python não interpretar a `\` de forma especial. Sempre use o `r` ao escrever expressões regulares.

Expressões regulares parecem assustadoras no começo, e é normal! Por enquanto, o importante é saber que elas existem e para que servem. Esse é um ótimo caso para pedir ajuda à IA, pedindo para ela explicar cada parte do padrão.

**Resumo**

- `os`: pastas, arquivos e caminhos
- `sys`: informações do Python e argumentos do terminal
- `datetime`: datas, horas e intervalos de tempo
- `re`: procurar, validar e substituir padrões em textos
