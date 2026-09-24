## Aula 2 de ambientes virtuais - Anaconda, ou Conda para os íntimos

Já vimos o como criar nossos ambientes com o `.venv`, agora vamos para uma das ferramentas mais queridinhas e conhecidas das pessoas que trabalham em dados, o `conda`. Ele é um gerenciador de pacotes e trabalha com alguns pontos importantes, como por exemplo em gerenciar o CUDA da NVIDIA - que é bem importante para quem trabalha com modelos de inteligência artificial. 

Outro ponto é que algumas bibliotecas de ciência de dados (NumPy, SciPy, bibliotecas de Machine Learning) não são escritas só em Python — por baixo, elas usam código em C ou Fortran pra rodar mais rápido
O pip às vezes tem dificuldade de instalar essas dependências "não-Python" corretamente, especialmente em certos sistemas operacionais
O conda foi criado justamente pra isso: ele gerencia não só bibliotecas Python, mas o próprio Python e dependências binárias junto

A primeira coisa que você precisa fazer é instalar o Anaconda - você pode entrar no [site deles](https://www.anaconda.com/download) e fazer o passo a passo encontrado lá. Temos duas versões do Anaconda que são disponibilizadas, que é o Anaconda Distribuiton e o Miniconda, e eu vou te explicar a diferença prática entre elas.

- **Anaconda Distribuiton:** é uma versão completa de tudo que você precisa, ou seja contém Python, o gerenciador conda, mais de 250 pacotes populares já pré-instalados (como NumPy, Pandas e Scikit-Learn) e uma interface gráfica que você pode usar, ao invés dos comandos em terminal. A principal **vantagem** é que ele está pronto para usar e por conta da interface é muito mais simples para quem está começando. A **desvantagem** é o seu tamanho, ele é um arquivo muito grande e demora muito para carregar a interface, o que pode ser um problema se seu computador não tiver tanta potência (espaço, memória RAM, etc.).
  
- **Miniconda:** a versão mini tem apenas o essencial: Python, o gerenciador conda e algumas dependências básicas. A maior **vantagem** dele é realmente ser muito leve, ocupa pouco espaço de armazenamento e você instala somente o que você vai usar. A **desvantagem** é que você não tem a interface gráfica, vai apenas usar a linha de comando no terminal.

Já que nós não temos medo de escrever códigos e comandos no nosso terminal, vamos optar pelo Miniconda.

Você pode usar o site para fazer o download e instalar, conforme o seu sistema operacional, ou fazer direto pela linha de comando. Se quiser saber um pouco mais em como fazer direto pela linha de comando, deixarei o passo a passo abaixo.

---
#### macOS (terminal)

```
mkdir -p ~/miniconda3
curl -o ~/miniconda3/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
```

Esse comando é para Apple Silicon (M1/M2/M3/M4), mas se  você tiver um Mac Intel, troque arm64 por x86_64 na URL.
Depois, ativar e inicializar:
```
source ~/miniconda3/bin/activate
conda init --all
```
Feche e abra o terminal de novo pra aplicar.

#### Linux (terminal)

```
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
```

Depois, mesma coisa:
```
source ~/miniconda3/bin/activate
conda init --all
```

Feche e abra o terminal de novo.

#### Windows (PowerShell)

No Windows você tem a opção de terminal "normal" e o terminal PowerShell, para isso você vai utilizar o PowerShell. 
```
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o miniconda.exe
Start-Process -FilePath ".\miniconda.exe" -ArgumentList "/S" -Wait
del miniconda.exe
```
O `/S` faz a instalação silenciosa (sem abrir janela gráfica), mas se você quiser ver o processo todo, apenas retire essa parte.

Depois de instalar, feche o PowerShell atual e abra um novo terminal chamado "Anaconda Prompt" (ou rode conda init powershell no PowerShell comum e reinicie)

A verificação nos três sistemas é a mesma. Depois de reabrir o terminal em qualquer sistema operacional:

```
conda --version
```

Se aparecer a versão instalada, e o prompt mostrar (base) no início da linha, deu certo!

---

Agora vamos ver a diferença de ativação/instalação do que já tinhamos visto usando venv e pip.

- Antes (venv):
```
python3 -m venv .venv
source .venv/bin/activate
```

- Agora (conda) - mesma ideia, mas os comandos são levemente diferentes.
  - Para criar um ambiente:
    `conda create --name meu_ambiente python=3.11 -y`
  - Para ativar o ambiente: `conda activate meu_ambiente`
  - Para instalar bibliotecas: `conda install pandas numpy -y`
  - Para desativar o ambiente: `conda deactivate`

Nos comandos conda, deixei explicito o `-y` que é basicamente para pular a verificação de "Você aceita instalar tudo que pediu?", usando o `-y` você já deixa pré-definido o `yes`, que é "Sim, li os termos e concordo".

### Mas e como posso instalar várias bibliotecas ao mesmo tempo? Existe o `requirements.txt` aqui?

Aqui existem duas opções, a primeira delas é continuar usando um arquivo de `requirements.txt` e instalar via `pip`, já que não é algo nativo do conda usar arquivos de texto para configurar ambiente; ou, você pode usar o jeito nativo do conda, que é um arquivo `.yml`, que salva tudo sobre o seu ambiente virtual, e geralmente o nome dele é `environment.yml`.

**Para a primeira opção, usando o `pip`**
Primeiro ative seu ambiente e depois faça a instalação usando o comando `pip`, que já vimos antes.

```
conda activate meu_ambiente
pip install -r requirements.txt
```

**Para a segunda opção, usando o arquivo `.yml`**
O arquivo `.yml` tem uma formatação um pouco mais específica do que o que vimos em um `.txt`.

```
name: meu_ambiente
channels:
  - defaults
dependencies:
  - python=3.12
  - pandas
  - numpy
```

Caso você tenha um arquivo `enviroments.yml`, para criar seu ambiente a partir dele, você pode usar o seguinte comando:

```
conda env create -f environment.yml
```

Mas se você já tem um ambiente feito e quer criar um documento `.yml`, você pode fazer algo semelhante ao que fizemos com o `pip freeze`.

```
conda env export > environment.yml
```

Então, para que fique fácil de você lembrar e comparar eles:

| | pip | conda |
|---|---|---|
| Arquivo de dependências | `requirements.txt` | `environment.yml` |
| Exportar | `pip freeze > requirements.txt` | `conda env export > environment.yml` |
| Instalar a partir do arquivo | `pip install -r requirements.txt` | `conda env create -f environment.yml` |

O Anaconda pode ser utilizado em diversos casos, principalmente quando falamos de machine learning, mas você pode você pode fazer o uso de qual gerenciador se sentir mais a vontade. Ainda temos mais dois casos para explorar, o **uv** e o **poetry**.