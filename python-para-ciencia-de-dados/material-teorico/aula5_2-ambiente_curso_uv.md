# Criar ambiente virtual UV 

## Criar a pasta do projeto 

```bash
mkdir ciencia-de-dados-estudos
cd ciencia-de-dados-estudos
```

Se você já tem uma pasta, basta entrar nela com `cd`.

## Iniciar o projeto

```bash
uv init
```
Isso cria os arquivos base:

- `pyproject.toml`: configuração do projeto e lista de dependências.
- `.python-version`: versão do Python que o projeto usa.
- `main.py`, `README.md` e `.gitignore`.


## Criar o ambiente com o nome personalizado

```bash
uv venv --prompt ciencia-de-dados
```

Isso cria a pasta `.venv` (o nome da pasta continua sendo `.venv`, que é o que o `uv` espera). O `--prompt` define apenas o texto que aparece no nosso terminal.

## Ativar o ambiente

```bash
source .venv/bin/activate
```

O terminal passa a mostrar que estamos dentro do ambiente virtual, com o `(ciencia_de_dados)` na esquerda da linha de comando do terminal.

---

Nós vamos fazer as instalações de dependências durante o decorrer das aulas, mas só para você lembrar como são os comandos de instalações, segue um breve tutorial.

## Instalar as dependências

```bash
uv add pandas numpy matplotlib scikit-learn
```

Para trabalhar com notebooks, adicione também:

```bash
uv add ipykernel jupyter
```

Esse comando instala os pacotes no `.venv`, registra no `pyproject.toml` e gera/atualiza o `uv.lock`.

Para ferramentas usadas apenas no desenvolvimento:

```bash
uv add --dev nome-do-pacote
```

## Usar o ambiente

```bash
python main.py            # roda com o ambiente ativado
uv run python main.py     # roda sem precisar ativar
uv run jupyter lab        # abre o Jupyter no ambiente
```

No VS Code, ao abrir um notebook, escolha o kernel **Python (.venv)** no canto superior direito.

## Desativar quando terminar

```bash
deactivate
```

## Reproduzir o ambiente em outro computador

Depois de clonar o repositório:

```bash
uv venv --prompt ciencia-de-dados
uv sync
source .venv/bin/activate
```

O `uv sync` instala as versões exatas registradas no `uv.lock`.

## Trocar o nome do prompt de um projeto existente

```bash
deactivate
rm -rf .venv
uv venv --prompt novo-nome
uv sync
source .venv/bin/activate
```

O `rm -rf .venv` apaga apenas o ambiente antigo. Seu código, o `pyproject.toml` e o `uv.lock` não são afetados.

## Pontos de atenção

- **A ordem importa:** crie o `.venv` com `--prompt` **antes** do primeiro `uv add`