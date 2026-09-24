
# UV — o gerenciador de pacotes mais rápido do ecossistema Python

## O que é o UV e quando surgiu

A primeira versão pública (0.1.0) foi lançada em **fevereiro de 2024** — ou seja, é a ferramenta mais recente entre as que vimos até agora (pip/venv, conda, Poetry).

## Por que o UV é diferente

- É escrito em **Rust**, não em Python — por isso consegue ser **dezenas a centenas de vezes mais rápido** que pip e Poetry em operações de instalação e resolução de dependências
- Não é só "mais um gerenciador de pacotes": ele **substitui várias ferramentas ao mesmo tempo** — pip, pip-tools, venv, virtualenv, pipx e até parte do papel do pyenv (gerenciamento de versões do Python), tudo numa ferramenta só
- Tem compatibilidade direta com o ecossistema pip existente (lê `requirements.txt`, entende comandos parecidos), facilitando a migração

## Por que usar UV em vez de Poetry

| | Poetry | UV |
|---|---|---|
| Velocidade | Rápido, mas escrito em Python | Extremamente rápido (Rust) |
| Gerencia versão do Python | Não — depende de pyenv/sistema | Sim, nativamente |
| Resolução de dependências | Própria (SAT solver) | Própria, otimizada em Rust |
| Migração de projeto existente | Manual | Comando dedicado (`uv add -r requirements.txt`) |
| Maturidade / tempo de mercado | Desde 2019, mais estável | Desde 2024, evolução rápida mas mais recente |
| Publicação no PyPI | Nativo (`poetry publish`) | Suporte mais recente, ainda evoluindo |

Não é uma questão de um ser "melhor" que o outro em tudo — o Poetry é mais maduro e testado em produção há mais tempo; o UV ganha em velocidade bruta e por unificar mais funções (incluindo gestão de versões do Python) numa ferramenta só. 

## Instalação

### macOS e Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Alternativa via Homebrew (macOS):
```bash
brew install uv
```

### Windows (PowerShell)

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Via pip (funciona nos 3 sistemas, mas não é o método recomendado)

```bash
pip install uv
```
> A Astral recomenda o instalador standalone (comandos acima) em vez do `pip install`, porque assim o UV fica isolado do seu Python e não depende de nenhum ambiente específico pra funcionar.

### Depois de instalar

**Reinicie o terminal** — é necessário para o terminal reconhecer o novo comando `uv` no PATH.

Verifique a instalação:
```bash
uv --version
```

## Inicializando um novo projeto

```bash
uv init
```

Esse comando cria vários arquivos na pasta atual:
- `.gitignore` — já configurado para projetos Python
- `.python-version` — arquivo que registra qual versão do Python o projeto usa
- `main.py` — arquivo inicial de exemplo
- `pyproject.toml` — o coração do projeto, onde ficam registradas todas as dependências
- `README.md`

## Rodando código com o UV

```bash
uv run main.py
```

Um benefício importante de rodar dessa forma: o UV identifica automaticamente se alguma dependência necessária para rodar o código está faltando, avisa (e/ou já baixa sozinho) antes de executar — evita o clássico erro de `ModuleNotFoundError` por esquecimento de instalação.

## Adicionando bibliotecas

```bash
uv add pandas
```

Quando você usa `uv add`, ele faz tudo de uma vez, de forma automática:
- Cria uma pasta `.venv` (ambiente virtual) — se ainda não existir
- Instala a biblioteca pedida e todas as suas dependências, de forma extremamente rápida
- Adiciona a biblioteca **e a versão instalada** diretamente no `pyproject.toml`
- Cria (ou atualiza) o arquivo `uv.lock`

### O arquivo uv.lock

Esse arquivo guarda todas as dependências do projeto — inclusive as dependências das próprias bibliotecas — com os links e versões exatas que foram instaladas. É o equivalente ao `poetry.lock`, mas gerado e atualizado automaticamente a cada `uv add`/`uv remove`, sem comando extra.

## Removendo bibliotecas

```bash
uv remove matplotlib
```

Remove a biblioteca, suas dependências que não são mais necessárias, e atualiza o `pyproject.toml` e o `uv.lock` automaticamente.

## Sincronizando o ambiente manualmente

Se você editar o `pyproject.toml` na mão (adicionar ou remover uma dependência diretamente no arquivo, sem usar `uv add`/`uv remove`), use:

```bash
uv sync
```

Esse comando sincroniza o ambiente virtual com o que está escrito no `pyproject.toml` — instala o que está faltando e desinstala o que não está mais listado.

## Gerenciamento de versões do Python

Diferente do Poetry, o UV também gerencia a **versão do Python** do projeto, não só as bibliotecas.

```bash
uv python list
```
Mostra as versões do Python disponíveis e instaladas pelo UV.

```bash
uv python install 3.12
```
Baixa e instala uma versão específica do Python, gerenciada pelo próprio UV — sem precisar do Homebrew, pyenv ou instalador do site oficial.

Para trocar a versão usada no projeto, você pode editar diretamente:
- O campo de versão dentro do `pyproject.toml`
- O arquivo `.python-version`

O UV também verifica compatibilidade: se uma biblioteca não tiver suporte pra versão do Python configurada no projeto, ele **recusa a instalação** em vez de instalar algo que provavelmente vai quebrar.

## Migrando um projeto existente para o UV

Se você já tem um projeto com `venv` + `requirements.txt` (ou qualquer setup anterior), migrar é algo simples:

1. Vá até a pasta do projeto existente
2. Rode a inicialização do UV:
   
```bash
uv init
```
Isso cria os arquivos padrão (`pyproject.toml`, `.python-version`, etc.) — mas ainda **sem** as dependências que você já tinha.

3. Importe as dependências do seu `requirements.txt` antigo:
```bash
uv add -r requirements.txt
```
Isso lê o arquivo antigo, instala tudo, e já registra cada biblioteca (com sua versão) no novo `pyproject.toml` e `uv.lock`.

## Para o Jupyter Notebook
Dentro do uv, precisamos criar um ambiente virtual para instalar o pacote chamado `ipykernel`, que nos permite efetivamente rodar códigos em Jupyter Notebook. 
```
uv venv
uv add ipykernel
```

Depois disso, você vai precisar selecionar esse ambiente virtual para os seus códigos.

## Referência

Documentação oficial: [docs.astral.sh/uv](https://docs.astral.sh/uv)