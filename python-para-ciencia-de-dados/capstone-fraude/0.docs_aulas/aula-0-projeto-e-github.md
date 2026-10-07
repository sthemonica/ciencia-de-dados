# Capstone Fraude — Aula 0: Preparando o projeto e o GitHub

Nas próximas aulas, vamos fazer um projeto completo de análise de dados: um **capstone** sobre fraude em compras online. Vamos carregar os dados, limpar, analisar e criar visualizações, usando NumPy, Pandas, Matplotlib, Seaborn e Plotly.

Antes de escrever qualquer análise, vamos preparar o projeto e conectar ele ao GitHub. Assim, todo o código fica salvo desde o primeiro dia.

**O case**

Somos o time de dados de um e-commerce. A empresa perdeu dinheiro com compras fraudulentas e quer entender: **o que diferencia uma compra fraudulenta de uma compra legítima?**

Recebemos 150 mil compras de março e abril de 2020, vindas de três sistemas diferentes:

- `compras_marco.xlsx`: compras de março, exportadas em Excel
- `compras_abril.csv`: compras de abril, exportadas em CSV
- `documentos.json`: quais documentos cada comprador entregou

Cada compra tem a coluna `fraude`, que vale `1` quando a compra foi fraudulenta e `0` quando foi legítima.

**Git e GitHub**

O **Git** é um programa que guarda o histórico do nosso código. Cada vez que salvamos uma versão, criamos um **commit**, como uma foto do projeto naquele momento. Se algo der errado, conseguimos voltar para uma foto anterior.

O **GitHub** é um site que guarda esse histórico na nuvem. Além de servir de backup, ele vira nosso portfólio: quem visitar o perfil consegue ver o projeto.

> Pense no Git como o "salvar" de um jogo. Você não salva só no final, salva em cada fase concluída. Se perder uma fase, volta para o último ponto salvo.

**Configurando o Git**

Na primeira vez que usamos o Git no computador, precisamos dizer quem somos. Esse nome e e-mail aparecem em cada commit:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

Use o mesmo e-mail da sua conta do GitHub.

**Criando o projeto com o uv**

```bash
uv init capstone-fraude
cd capstone-fraude
```

O `uv init` cria a pasta do projeto com alguns arquivos:

- `pyproject.toml`: a "ficha" do projeto, com nome, versão do Python e bibliotecas
- `README.md`: a apresentação do projeto, que aparece na página do GitHub
- `.gitignore`: lista de arquivos que o Git deve ignorar
- `main.py`: um arquivo de exemplo, que podemos apagar

O `uv init` também já cria um repositório Git na pasta, então não precisamos rodar o `git init`.

**Organizando as pastas**

Um projeto de dados bem organizado separa os dados originais, o código e os resultados:

```text
capstone-fraude/
├── data/
│   ├── raw/          # dados originais, nunca são alterados
│   └── processed/    # dados gerados pelos notebooks
├── notebooks/        # um notebook para cada etapa
├── reports/
│   └── figures/      # gráficos para apresentação
└── pyproject.toml
```

```bash
mkdir -p data/raw data/processed notebooks reports/figures
```

Copie os três arquivos de dados para a pasta `data/raw`.

A regra mais importante: **nunca alteramos os arquivos da pasta `raw`**. Toda limpeza é feita no código, e o resultado é salvo em `processed`. Assim, sempre conseguimos refazer a análise do zero.

**Instalando as bibliotecas**

```bash
uv add pandas openpyxl ipykernel
```

- `pandas`: análise de dados (o NumPy é instalado junto, porque o Pandas depende dele)
- `openpyxl`: permite ao Pandas ler arquivos do Excel
- `ipykernel`: permite rodar notebooks no VS Code usando o ambiente do projeto

As bibliotecas de gráficos vamos instalar quando chegar a hora de usar.

Para rodar os notebooks, abra a pasta no VS Code, crie um arquivo `.ipynb` dentro de `notebooks` e, no canto superior direito, selecione o kernel `.venv` do projeto.

**Ignorando arquivos**

Nem tudo deve ir para o GitHub. A pasta `.venv`, por exemplo, tem as bibliotecas instaladas e é enorme. O `uv init` já colocou ela no `.gitignore`.

Os arquivos de `data/processed` também não precisam ir, porque os notebooks recriam eles. Adicione no final do `.gitignore`:

```text
# Dados gerados pelos notebooks (podem ser recriados)
data/processed/*
!data/processed/.gitkeep
```

O Git não salva pastas vazias. Por isso, criamos um arquivo vazio chamado `.gitkeep` dentro de `processed`, e a linha com `!` diz para o Git **não** ignorar esse arquivo:

```bash
touch data/processed/.gitkeep
```

**Primeiro commit**

```bash
git add .
git commit -m "Cria estrutura do projeto e adiciona dados brutos"
```

- `git add .`: escolhe todos os arquivos novos e alterados para entrar no próximo commit
- `git commit -m "..."`: cria o commit com uma mensagem explicando o que mudou

Antes do `commit`, vale rodar `git status` para conferir quais arquivos vão entrar.

**Enviando para o GitHub**

No GitHub, clique em **New repository**, dê o nome `capstone-fraude` e crie o repositório **sem** marcar a opção de README (já temos um). O GitHub vai mostrar o endereço do repositório. Depois, no terminal:

```bash
git branch -M main
git remote add origin https://github.com/seu-usuario/capstone-fraude.git
git push -u origin main
```

- `git branch -M main`: garante que o nome da branch principal seja `main`
- `git remote add origin ...`: conecta a pasta ao repositório do GitHub
- `git push -u origin main`: envia os commits. O `-u` faz o Git lembrar o destino, então nas próximas vezes basta `git push`

Atualize a página do GitHub e os arquivos vão aparecer lá!

**A rotina de cada aula**

Ao final de cada aula, vamos salvar o progresso:

```bash
git add .
git commit -m "Mensagem explicando o que foi feito"
git push
```

Boas mensagens de commit explicam **o que** mudou: `Adiciona limpeza de valores ausentes` é muito melhor que `atualização` ou `aaa`.

**Resumo**

- O Git guarda o histórico do código em commits, e o GitHub guarda esse histórico na nuvem
- `uv init` cria o projeto já com Git, e `uv add` instala as bibliotecas
- Dados originais ficam em `data/raw` e nunca são alterados
- O `.gitignore` evita enviar arquivos grandes ou que podem ser recriados
- Ao final de cada aula: `git add .`, `git commit -m "..."` e `git push`
