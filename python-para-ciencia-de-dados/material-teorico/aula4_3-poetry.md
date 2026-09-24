# Poetry — gestão moderna de dependências em Python

Quando usamos apenas pip + venv, gerenciar versões pode ficar complicado: o `requirements.txt` trava a versão das bibliotecas que você pediu diretamente, mas **não trava as dependências das próprias dependências** — isso pode causar conflitos meses depois, quando uma dependência indireta atualiza sozinha.

## O que é o Poetry e quando surgiu

O Poetry foi lançado oficialmente em **dezembro de 2019**. Ele nasceu inspirado em gerenciadores de pacotes de outras linguagens que já resolviam, trazendo para o Python um único arquivo, uma única ferramenta e as dependências com suas versões e detalhes, para que nada quebre sem porquê.

## Instalação

O Poetry tem um instalador oficial multiplataforma (`install.python-poetry.org`) que funciona de forma parecida nos três sistemas operacionais, além da opção via Homebrew no macOS.

### macOS

**Opção 1 — via Homebrew (mais simples):**
```bash
brew install poetry
```

**Opção 2 — instalador oficial:**
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Linux

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Depois de instalar, adicione o Poetry ao PATH (o instalador avisa o caminho exato ao final, geralmente `$HOME/.local/bin`):
```bash
export PATH="$HOME/.local/bin:$PATH"
```

### Windows (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```
> Se o Python foi instalado pela Microsoft Store, troque `py` por `python` no comando acima.

### Verificando a instalação (igual nos 3 sistemas)

```bash
poetry --version
```

## Criando o projeto

```bash
poetry init --no-interaction
```

Isso cria um arquivo `pyproject.toml` — ele guarda as dependências do projeto de forma organizada.

## O arquivo pyproject.toml

Já vimos o `.txt` sendo usado pelo pip e o `.yml` pelo conda. Agora conhecemos o `.toml`, usado pelo Poetry.

A diferença principal: o `pyproject.toml` não é *só* uma lista de bibliotecas — é um arquivo de configuração completo do projeto, dividido em seções (`[tool.poetry]`, `[tool.poetry.dependencies]`, etc.), guardando nome do projeto, versão, autor, dependências e até configurações de build/publicação, tudo num lugar só.

### Vantagens em relação ao requirements.txt e ao environment.yml

| | requirements.txt / environment.yml | pyproject.toml (Poetry) |
|---|---|---|
| Trava dependências indiretas | Não (requirements.txt) | Sim, via `poetry.lock` |
| Resolução de conflitos | Manual, você resolve na mão | Resolvedor automático (SAT solver) — verifica compatibilidade antes de instalar |
| Um arquivo só pro projeto inteiro | Não — precisa de `setup.py` separado pra empacotar | Sim — dependências, metadados e build ficam juntos |
| Publicar a biblioteca no PyPI | Precisa de ferramentas extras | Nativo: `poetry build` + `poetry publish` |
| Ambiente virtual | Você cria manualmente (`venv`/`conda create`) | Poetry cria e gerencia automaticamente |

A vantagem central: com `requirements.txt`, se a biblioteca X depende da biblioteca Y, e a Y atualiza sozinha pra uma versão incompatível, você só descobre quando o código quebrar. O Poetry resolve essa árvore de dependências **antes** de instalar qualquer coisa, e trava tudo no arquivo `poetry.lock` — garantindo que o ambiente é idêntico em qualquer máquina.

## Comandos principais

### Adicionar e remover bibliotecas

```bash
poetry add pandas
```
Instala a biblioteca e suas dependências, e já adiciona o nome + versão no `pyproject.toml`.

```bash
poetry remove pandas
```
Remove a biblioteca e limpa a entrada correspondente do `pyproject.toml`.

### Controlando versões na instalação

```bash
poetry add requests@2.31.0
```
O `@` fixa a instalação **exatamente** nessa versão.

```bash
poetry add requests^2.31.0
```
O `^` (circunflexo) instala a partir dessa versão, aceitando atualizações futuras **compatíveis** (não quebra a API). É o formato mais recomendado no dia a dia — no `pyproject.toml`, a dependência fica registrada com o `^` junto.

```bash
poetry add requests~2.31.0
```
O `~` (til) permite apenas atualizações de **patch** (ex: 2.31.0 → 2.31.9, mas não 2.32.0) — mais restritivo que o `^`.

> **Regra prática:** o `^` é o mais usado no dia a dia, por equilibrar segurança e liberdade de atualização.

### Visualizando dependências

```bash
poetry show
```
Lista todas as bibliotecas instaladas e suas versões.

```bash
poetry show pandas
```
Mostra detalhes de uma biblioteca específica: versão instalada, descrição, e quais outras bibliotecas foram instaladas como dependência dela.

```bash
poetry show --tree
```
Mostra a árvore de dependências completa — útil pra visualizar quem depende de quem.

```bash
poetry show --outdated
```
Mostra quais bibliotecas têm versões mais novas disponíveis.

### O arquivo poetry.lock

Junto com o `pyproject.toml`, o Poetry cria o `poetry.lock` — esse arquivo guarda a versão exata de **cada** dependência (inclusive as indiretas), junto com o hash de cada pacote. É esse arquivo que garante que, ao instalar o projeto em outra máquina, todo mundo recebe exatamente as mesmas versões.

### Instalando um projeto existente

```bash
poetry install
```
Lê o `pyproject.toml`/`poetry.lock` e instala todas as dependências — é o equivalente ao `pip install -r requirements.txt`.

```bash
poetry install --no-root
```
Instala as dependências, mas **sem** instalar o próprio projeto atual como pacote — útil quando você só quer o ambiente, sem empacotar o código local.

```bash
poetry sync
```
Instala exatamente o que está no `poetry.lock` e **remove** qualquer pacote que não esteja listado ali — garante que o ambiente fique idêntico ao lockfile, sem "sobras" de instalações antigas.

### Ativando o ambiente virtual do Poetry

O Poetry cria automaticamente um ambiente virtual isolado pra cada projeto — a mesma ideia de "gaveta" que já vimos com `venv` e `conda`.

```bash
poetry env activate
```
Ativa o ambiente virtual do projeto atual. (Nas versões mais antigas do Poetry, esse comando era `poetry shell` — hoje ele foi movido pra um plugin opcional, então `poetry env activate` é o caminho padrão recomendado.)

```bash
poetry env list
```
Mostra os ambientes virtuais criados para o projeto.

### Rodando um comando sem ativar o ambiente

```bash
poetry run python script.py
```
Executa um comando dentro do ambiente do Poetry, sem precisar ativá-lo antes — útil pra scripts rápidos ou automações.

### Versionamento do projeto

O Poetry também ajuda a versionar seu próprio projeto, seguindo o padrão de versionamento semântico (MAJOR.MINOR.PATCH).

```bash
poetry version minor
```
Se o projeto está na versão `0.1.0`, esse comando avança para `0.2.0`.

Outras opções de versionamento semântico:
```bash
poetry version patch   # 0.1.0 → 0.1.1
poetry version major   # 0.1.0 → 1.0.0
```

### Publicando o projeto

```bash
poetry build
```
Gera os arquivos de distribuição do projeto (necessário antes de publicar).

```bash
poetry publish
```
Publica o projeto no PyPI (ou em outro repositório configurado) — transforma seu código num pacote instalável via `pip install`.