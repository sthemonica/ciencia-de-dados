## Programar é dar instruções

Programar é, no fundo, dar instruções para algo que só faz **exatamente** o que você disser — nada além, nada de "óbvio" ou "subentendido".

Hoje vamos aprender os 3 tipos de instrução que resolvem quase qualquer problema de lógica.

## Pilar 1 — Sequência (fazer as coisas em ordem)

Vamos pensar em como nós fazemos as coisas no dia a dia, como por exemplo "Como escovamos os dentes?"
1. pegar a escova de dentes
2. colocar a pasta
3. escovar os dentes
4. enxaguar a boca

Essa ordem é importante, já que imagina trocar o item 2 com o item 4, você enxagua a boca antes de escovar os dentes e depois de escovar eles coloca a pasta. Não faz nem sentido. Então a lógica é importante!

Basicamente, um programa é uma lista de instruções que o computador segue **de cima para baixo, em ordem** — exatamente como uma receita ou uma rotina do dia a dia.

## Pilar 2 — Decisão (fazer diferente dependendo da situação)

Mais uma vez vamos pensar em coisas do nosso cotidiano:
- "Se estiver chovendo, o que a gente faz?" → leva guarda-chuva
- "E se não estiver?" → não leva

Então basicamente nós temos duas opções nesse momento:

```
Está chovendo?
 |
 +-- Sim --> Levar guarda-chuva
 |
 +-- Não --> Não levar
```

Isso **é** a lógica de um `if/else` do Python, mas em português podemos pensar em `se/se não`.

Outro exemplo é quando precisamos fazer uma prova e dependendo da sua nota, você tem classificações. A mais básica delas é, se você tirou acima da média (6), você passou na prova, se não você precisa repetir o teste.

```
Como foi a nota da prova?
 |
 +-- 6 ou + --> Passou na prova!
 |
 +-- Menos que 6 (média) --> Repetir o teste :(
```

## Pilar 3 — Repetição (fazer a mesma coisa várias vezes)

Em mais um momento de exemplos do nosso dia a dia, podemos pensar sobre uma das tarefas mais chatas de cuidar na casa, lavar a louça.
- "Quando a gente lava louça, lava um prato só ou repete até acabar?"
- "A gente sabe de antemão quantos pratos tem, ou vai lavando até não sobrar mais nenhum?"

Ou seja, aqui temos duas situações bem diferentes. Onde podemos pensar que em um restaurante é comum de acontecer a segunda opção, principalmente em horários de pico, mas na sua casa você geralmente tem um controle maior da quantidade de louça.
Então as opções que temos para repetição são:

- **Repetir um número certo de vezes** (ex: fazer 10 flexões) - comparado ao `for` no Python
- **Repetir até algo acontecer** (ex: correr até cansar) - comparado ao `while` no Python

---

Nós já pensamos de uma forma lógica todos os dias, sempre tem algum jeito de otimizar algum processo ou de pensar em novas soluções, e é a mesma coisa quando falamos em códigos. O que nós vamos ver daqui em diante são a base, mas você pode pensar em soluções que são melhores do que as mostradas, ou só diferentes. 