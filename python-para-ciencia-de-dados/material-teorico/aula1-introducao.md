## O que é Python e por que é a linguagem das pessoas que trabalham com dados

### Por que Python virou a linguagem de referência em dados

- **Sintaxe simples e legível** — o código Python se parece muito com pseudocódigo, o que reduz a barreira de entrada pra quem está aprendendo
- **Ecossistema gigante de bibliotecas especializadas**:
  - `Pandas` — manipulação e análise de dados tabulares
  - `NumPy` — computação numérica e arrays multidimensionais
  - `Matplotlib` / `Seaborn` — visualização de dados
  - `Scikit-learn` — machine learning
  - `Jupyter` — notebooks interativos, ideais para explorar dados passo a passo
- **Comunidade extremamente ativa** — praticamente qualquer problema de dados já tem uma biblioteca pronta ou uma solução documentada
- **Não é uma linguagem "de nicho"** — a mesma linguagem serve para automação, backend, IA e ciência de dados, o que torna o aprendizado um investimento que se paga em múltiplas frentes da carreira

---

## Por que Python depois de SQL — diferenças práticas

### O ponto de partida: SQL já ensinou a pensar em dados

Quem aprende SQL primeiro já desenvolveu uma habilidade importante: pensar em dados como **tabelas** e formular perguntas estruturadas sobre esses mesmos dados. O Python constrói em cima dessa base, mas muda o tipo de raciocínio.

### Diferenças práticas

| | SQL | Python |
|---|---|---|
| Propósito | Consultar e manipular dados dentro de um banco | Programação geral: dados, automação, ML, web |
| Estrutura |você diz *o quê* quer | você diz *como* quer fazer, passo a passo |
| Onde roda | Dentro do banco de dados | Em qualquer lugar (seu PC, servidor, nuvem) |
| Bibliotecas disponíveis | Limitadas ao padrão SQL (mais funções do próprio banco) | Ecossistema amplo: Pandas, NumPy, Scikit-learn, Matplotlib, etc. |
| Curva de aprendizado | Rápida para o básico | Mais ampla, porém modular — você aprende por partes |


Ou seja, o SQL ensina você a pensar em dados como **tabelas que você consulta** e o Python ensina você a pensar em dados como **objetos que você transforma com lógica**.


---

## O que SQL não consegue responder e onde Python entra

### O que SQL faz muito bem

SQL é ótimo para buscar, filtrar e agregar dados que **já estão estruturados** em tabelas. Perguntas como:
- "Quantos clientes compraram em março?"
- "Qual a média de vendas por região?"
- "Quais produtos tiveram queda de estoque no último trimestre?"

SQL responde **perguntas sobre os dados que já existem.**

### Onde SQL trava

- **Machine Learning e previsões** — SQL não tem como treinar um modelo que aprende padrões e faz previsões sobre dados novos
- **Dados não estruturados** — texto livre, imagens, arquivos JSON aninhados, respostas de APIs — tudo isso foge do modelo de tabelas do SQL
- **Lógica condicional complexa e loops** — simular cenários, iterar sobre combinações, repetir um processo até uma condição ser satisfeita
- **Conectar múltiplas fontes de dados diferentes** — juntar um banco de dados com uma planilha, uma API e um arquivo de log, tudo no mesmo processo
- **Automação e web scraping** — coletar dados de sites, automatizar tarefas repetitivas
- **Visualizações estatísticas avançadas e testes de hipótese** — análises que vão além de somas e médias
- **Reutilização de lógica** — funções, testes automatizados, pipelines que rodam sozinhos periodicamente


### Por que isso importa na prática

Um cientista de dados frequentemente usa as duas ferramentas em conjunto: SQL para **extrair** os dados de um banco de forma eficiente, e Python para **processar, analisar, modelar e visualizar** o que SQL sozinho não conseguiria fazer. Não é uma substituição — é uma continuação natural do que SQL já começou.