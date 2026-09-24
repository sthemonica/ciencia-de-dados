# Fundamentos de Computação para Ciência de Dados

## Como os computadores funcionam e o que é uma linguagem de programação

### O computador só entende uma coisa

No nível mais básico, um computador só reconhece **eletricidade ligada ou desligada**. Essa informação é representada em **binário** — sequências de 0 e 1. Todo texto, imagem, música e programa existente é, no fundo, uma sequência de binário armazenada e processada por circuitos eletrônicos.

Por exemplo, se eu fosse escrever Brasil em binário, seria dessa forma:
**01000010 01110010 01100001 01110011 01101001 01101100**

Cada conjunto de 8 números de zeros e uns formam um bit, que carrega uma informação. Se quiser testar outras palavras ou frases, procure um tradutor binário.

### Camadas de tradução

Ninguém escreve programas diretamente em binário — até porque seria impraticável lembrar de todas as combinações. Por isso, existem **camadas de abstração** entre o que a máquina entende e o que um humano consegue escrever:

```
Código em Python (alto nível)
        |
Interpretador traduz
        |
Linguagem de máquina (binário)
        |
Processador executa
```

- **Linguagem de baixo nível** (ex: Assembly) — muito próxima do binário, difícil de ler para humanos, mas dá controle direto sobre o hardware
- **Linguagem de alto nível** (ex: Python, SQL, Java) — parecida com a linguagem humana, como português/inglês. Ela é estruturada, fácil de escrever e entender

### O que é uma linguagem de programação

Uma linguagem de programação é uma forma de **traduzir intenção humana em instruções que o processador executa**. Cada linguagem tem suas próprias regras (sintaxe), assim como um idioma tem gramática — e um **tradutor** (compilador ou interpretador) faz a conversão entre o que você escreve e o que a máquina realmente executa.

### Compilado vs. Interpretado

- **Compilado** (ex: C, C++): todo o código é traduzido para binário de uma vez, e só gera o resultado final. O resultado é um executável rápido, mas qualquer mudança exige recompilar tudo e levar mais tempo entendendo o que mudar.
- **Interpretado** (ex: Python): o código é traduzido e executado **linha por linha**, em tempo real. É mais lento que uma linguagem compilada, mas permite testar e explorar código de forma interativa — por isso é tão usado em ciência de dados, onde você está constantemente testando ideias e validando elas.

