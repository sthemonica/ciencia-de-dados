- ⁠Tratamento de erros: try, except e raise

Dentro da execução do nosso código, podem acontencer erros inesperados, como tentar abrir um arquivo cujo o nome não existe ou já foi deletado.

Para lidar com essas situações, toda linguagem de programação tem um estrutura para tratamento de erros.

**try e except**

No Python, criamos dois blocos em conjunto para essa situação:

- `try`: para testar se todo o código dentro desse bloco pode soltar um erro, não interrompendo a execução do restante do código
- `except`: para tratar um possível erro que o bloco try

```python
# arquivo ler_arquivo.py
try:
    arquivo = open("meu_texto.txt")
    print("Arquivo aberto!")
except:
    print("Não foi possível acessar o arquivo")
```

Nesse código, estamos tentanto acessar o arquivo `meu_texto.txt`.

- Se for o caso do arquivo não existir, o bloco `except` vai ser executado, mostrando a mensagem que não foi acessar o arquivo.
- Caso o arquivo exista, a mensagem `Arquivo aberto!` será mostrada.

**raise**

Além disso, em alguns casos, podemos querer causar um erro na nossa aplicação propositalmente, caso o usuário tenha informado algum dado inválido por exemplo.

Para gerar esse erro, basta usar a palavra chave `raise` e chamar alguma classe de erro, por enquanto vamos usar a `Exception`.

```python
# arquivo numero.py
numero = input("Digite um número: ")
numero = int(numero)
if numero != 0:
    raise Exception("O número deve ser diferente de zero")

print(1000 / numero)
```

Nesse código, estamos testando se a variável `numero`, onde o usuário vai adicionar um número, vai ser diferente de 0.

Se for, vamos cancelar a operação, porque o nosso código irá dividir `1000` pela variável, e nenhum número pode ser divido por zero.

Nesse caso, não estamos tratando o erro com os blocos `try` e `exception`, mas isso pode ser uma opção! Em alguns momentos, podemos querer que o error aconteca para a execução do programa ser interrompida, evitando, no nosso exemplo anterior, uma divisão inválida.

- ⁠Boas práticas: nomes claros, comentários e PEP8

Um código não é escrito só para o computador entender, ele também é escrito para pessoas lerem, inclusive você mesmo daqui a alguns meses.
O Python executa um código bagunçado sem reclamar, mas quem vai precisar corrigir ou melhorar esse código vai sofrer bastante.

**Nomes claros**

O nome de uma variável ou função deve dizer o que ela guarda ou o que ela faz.

```python
# arquivo nomes_ruins.py
a = 25
b = 4
c = a * b

def f(x):
    return x * 0.9
```

```python
# arquivo nomes_bons.py
preco_unitario = 25
quantidade = 4
preco_total = preco_unitario * quantidade

def aplicar_desconto(valor):
    return valor * 0.9
```

Os dois códigos fazem a mesma coisa, mas no segundo não precisamos adivinhar nada. Só de ler, já sabemos que estamos calculando o preço total de uma compra e aplicando um desconto.

Algumas dicas:
- Evite nomes de uma letra só (exceto em casos bem curtos e índices, como `for i in range(10)`)
- Funções geralmente fazem uma ação, então use verbos: `calcular_media`, `enviar_email`, `validar_idade`
- Variáveis guardam coisas, então use substantivos: `nome_cliente`, `lista_de_notas`, `total`

**Comentários**

Comentários são linhas que o Python ignora, servem apenas para explicar algo para quem está lendo. Usamos `#` para comentários de uma linha.

Um bom comentário explica **por que** algo foi feito, e não **o que** o código faz, afinal, o código já mostra o que faz.

```python
# Comentário desnecessário: repete o que o código já diz
idade = idade + 1  # soma 1 na idade

# Comentário útil: explica o motivo
idade = idade + 1  # o sistema antigo salvava a idade do ano anterior
```

Para explicar o que uma função faz, usamos a **docstring**, um texto entre três aspas logo na primeira linha da função:

```python
def calcular_media(notas):
    """Recebe uma lista de notas e retorna a média entre elas."""
    return sum(notas) / len(notas)
```

**PEP8**

A PEP8 é o guia oficial de estilo do Python. Ela é um conjunto de combinados da comunidade para que todo código Python tenha uma "cara" parecida, independente de quem escreveu.

As principais regras:
- Variáveis e funções em `snake_case` (letras minúsculas separadas por `_`): `nome_completo`, `calcular_total`
- Classes em `PascalCase` (cada palavra começa com maiúscula): `ContaBancaria`, `Cliente`
- Constantes (valores que não mudam) em letras maiúsculas: `TAXA_DE_JUROS = 0.05`
- Indentação com 4 espaços
- Espaços ao redor de operadores: `total = a + b` e não `total=a+b`
- Linhas com no máximo 79 caracteres
- Duas linhas em branco entre funções

```python
# arquivo fora_do_padrao.py
def CalcularTotal(Preco,Qtd):
  return Preco*Qtd
def mostrarTotal(t):
  print(t)
```

```python
# arquivo no_padrao.py
def calcular_total(preco, quantidade):
    return preco * quantidade


def mostrar_total(total):
    print(total)
```

Não precisa decorar tudo! Existem ferramentas que verificam e até corrigem o código automaticamente, como o **Ruff**, o **Black** e o **Flake8**, e a maioria dos editores (como o VS Code) consegue usá-las.

Pense nas boas práticas como a letra num caderno: dá para escrever de qualquer jeito e você até entende na hora, mas se outra pessoa precisar ler, ou você mesmo daqui a um mês, uma letra legível faz toda a diferença.

---

- ⁠Como usar IA para escrever, entender e depurar código sem perder o raciocínio próprio

Ferramentas de IA, como o ChatGPT, o Claude e o GitHub Copilot, conseguem escrever código, explicar trechos que não entendemos e ajudar a encontrar erros. Elas são ótimas mas se a IA pensa tudo por você, você não aprende a programar, só aprende a copiar e colar.

Um exemplo disso é o GPS. Se você sempre usa o GPS para ir a qualquer lugar, depois de anos morando na cidade ainda não sabe andar por ela sozinho. A IA funciona da mesma forma: use como apoio, não como substituta do seu raciocínio.

**Para escrever código**

Antes de pedir para a IA, tente resolver sozinho, nem que seja uma versão incompleta ou em comentários. Depois, use a IA para comparar com a sua solução ou para destravar a parte em que você empacou.

```text
ERRADO!

Faz um programa que calcula a média de notas
```

```
CORRETO!

Escrevi essa função para calcular a média de notas, mas não sei
como tratar o caso da lista vazia. Pode me dar uma dica, sem me
dar a resposta pronta?
```

**Para entender código**

Quando encontrar um código que não entende, peça para a IA explicar linha por linha, e depois tente explicar com suas próprias palavras. Uma boa regra: **nunca use um código que você não conseguiria explicar para outra pessoa**. No trabalho, nós somos as pessoas responsáveis pelo código, precisamos entender ele para poder responder qualquer situação que possa acontecer.

```text
"Explique linha por linha o que esse código faz, como se eu
estivesse começando a programar agora."

"Por que aqui foi usado um for e não um while?"
```

**Para depurar código**

Quando um erro aparecer, antes de colar tudo na IA:
1. Leia a mensagem de erro. O Python diz o tipo do erro e a linha onde ele aconteceu
2. Tente formular uma hipótese: "acho que o erro é porque..."
3. Só então peça ajuda, enviando o código, a mensagem de erro e o que você esperava que acontecesse

```python
# arquivo dobro.py
numero = input("Digite um número: ")
print(numero * 2)
```

Se digitarmos `5`, o resultado será `55` e não `10`. Uma boa pergunta para a IA seria:

```text
Meu código deveria mostrar o dobro do número digitado, mas quando
   digito 5 aparece 55. Acho que o problema está no input. Por que
   isso acontece?
```

Assim, a IA vai te explicar que o `input` sempre retorna um texto (string), e que multiplicar um texto por 2 repete ele duas vezes. Você aprendeu o conceito, e não só recebeu o código corrigido: `int(input(...))`.

**Cuidados importantes**
- A IA pode errar e às vezes inventa funções que não existem, com muita confiança. Sempre teste o código antes de considerar que está certo
- Não cole senhas, chaves de acesso ou dados pessoais de outras pessoas em ferramentas de IA
- Se a IA sugeriu algo e você não entendeu, pergunte de novo. Não existe pergunta boba para a IA

A IA deve ser como um professor paciente disponível a qualquer hora, e não como um colega que faz a prova no seu lugar.