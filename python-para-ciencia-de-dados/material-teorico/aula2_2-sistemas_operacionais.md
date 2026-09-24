---

## Sistemas operacionais para ciência de dados: Windows, Linux e macOS — diferenças práticas

O sistema operacional é a camada de software que gerencia o hardware do computador (processador, memória, arquivos) e permite que outros programas rodem sobre ele. Windows, Linux e macOS são as três opções mais comuns no mercado.

Podemos dizer que o **Linux e macOS compartilham uma base conceitual parecida**, enquanto o Windows segue uma filosofia própria — e é por isso que comandos de terminal, caminhos de arquivo e certas ferramentas se comportam de forma diferente nele.

### Diferenças práticas para quem trabalha com dados

| | Windows | Linux | macOS |
|---|---|---|---|
| Terminal padrão | PowerShell / CMD | Bash/Zsh (nativo) | Zsh (nativo, via Terminal.app) |
| Compatibilidade com ferramentas de dados | Boa, mas com mais atritos (paths, permissões) | Excelente — padrão em servidores e nuvem | Excelente — muito próxima do Linux |
| Ambiente de produção mais comum | Raro em servidores de ML/dados | É o padrão de fato em nuvem e produção | Comum em máquinas de desenvolvimento, raro em servidor |
| Gerenciador de pacotes do sistema | Nenhum nativo (usa Chocolatey/Winget) | apt, dnf, pacman, etc. (nativo) | Homebrew (não nativo, mas padrão de mercado) |
| GPU para Machine Learning | Suporte via drivers próprios | Suporte mais maduro para CUDA/NVIDIA | Suporte mais limitado a GPUs NVIDIA |

### O motivo prático de tanta gente usar Linux (ou WSL) em dados

A maioria dos ambientes de nuvem, servidores de produção e clusters de treinamento de modelos roda **Linux** — geralmente Ubuntu. Isso significa que um projeto de dados desenvolvido em Linux tende a ir para produção sem grandes atritos, porque o ambiente de desenvolvimento já é parecido com o de produção.

Por conta disso, muitos profissionais que usam Windows recorrem ao **WSL (Windows Subsystem for Linux)** — uma camada que permite rodar uma distribuição Linux completa (como o Ubuntu) dentro do próprio Windows, sem precisar de uma máquina separada ou dual-boot (ter o Linux e o Windows na mesma máquina!). 

Então, podemos dizer que:
- **macOS**: a maioria dos comandos e ferramentas funciona sem ajuste
- **Linux**: é o ambiente mais alinhado ao que se usa em produção — ótima escolha se você já está *confortável* nele
- **Windows**: funciona bem para aprender e desenvolver, mas vale considerar o WSL se você for trabalhar com ferramentas mais pesadas de dados/ML no futuro

Nenhum dos três é "errado" para começar — a diferença aparece mais adiante, quando o projeto precisar rodar em um servidor ou na nuvem. 

**Vale lembrar também que o sistema operacional que você tem, seja ele qual for, vai suprir o seu momento atual!**

O sistema que eu estou utilizando é o macOS, mas por muito tempo da vida usei o Windows com WSL. Mesmo trabalhando com programação há 12 anos, não me adaptei ainda ao Linux, e tá tudo bem!

---

## Terminal e linha de comando: navegação, manipulação de arquivos e automação básica

Você sabe o que é terminal? Já viu algum filme onde as pessoas mostram hackers usando apenas o teclado, digitando tudo e fazendo todos os sistemas cairem, roubando dados ou algo assim? Não tem nada a ver com o que faremos, mas aquela interface é a de um terminal de comando.
O terminal permite fazer, com uma linha de texto, tarefas que levariam vários cliques numa interface gráfica — e permite **automatizar** essas tarefas, algo que a interface gráfica não oferece. Para ciência de dados nós podemos rodar scripts, instalar bibliotecas, mover arquivos entre pastas de projeto, tudo isso passa pelo terminal no dia a dia. 

### Navegação básica (comandos essenciais)

| O que você quer fazer | Comando |
|---|---|
| Ver em qual pasta você está | `pwd` (macOS/Linux) — no PowerShell, `pwd` também funciona |
| Listar arquivos e pastas | `ls` (macOS/Linux) / `dir` (Windows CMD) — no PowerShell, `ls` também funciona |
| Listar incluindo arquivos ocultos | `ls -a` |
| Entrar em uma pasta | `cd nome_da_pasta` |
| Voltar para a pasta anterior | `cd ..` |
| Ir direto para a pasta pessoal (home) | `cd ~` (macOS/Linux) |

> **Nota importante:** no macOS e Linux, o terminal diferencia maiúsculas de minúsculas (`Documentos` é diferente de `documentos`). No Windows, isso normalmente não faz diferença.

### Manipulação de arquivos e pastas

| O que você quer fazer | macOS / Linux | Windows (PowerShell) |
|---|---|---|
| Criar uma pasta | `mkdir nome_pasta` | `mkdir nome_pasta` |
| Criar um arquivo vazio | `touch arquivo.py` | `New-Item arquivo.py` |
| Copiar um arquivo | `cp origem.txt destino.txt` | `Copy-Item origem.txt destino.txt` |
| Mover ou renomear um arquivo | `mv nome_antigo.txt nome_novo.txt` | `Move-Item nome_antigo.txt nome_novo.txt` |
| Apagar um arquivo | `rm arquivo.txt` | `Remove-Item arquivo.txt` |
| Apagar uma pasta e tudo dentro dela | `rm -r nome_pasta` | `Remove-Item -Recurse nome_pasta` |
| Ver o conteúdo de um arquivo de texto | `cat arquivo.txt` | `Get-Content arquivo.txt` |

> **Atenção:** o comando de apagar pasta (`rm -r` ou `Remove-Item -Recurse`) apaga tudo **sem pedir confirmação** e sem enviar para a lixeira — ou seja, não tem como voltar atrás!

### Alguns recursos do terminal

- **Autocompletar com Tab**: comece a digitar o nome de um arquivo ou pasta e aperte Tab — o terminal completa automaticamente (ou mostra as opções, se houver mais de uma)
- **Setas para cima/baixo**: navegam pelo histórico de comandos já digitados, evitando redigitar tudo
- **Limpar a tela**: `clear` (macOS/Linux) ou `cls` (Windows CMD) — útil pra manter a leitura organizada

### Automação básica: por que isso importa em dados

Um dos maiores ganhos do terminal é poder **encadear comandos** e criar scripts simples que automatizam tarefas repetitivas — por exemplo, rodar um script Python toda vez que um novo arquivo chega numa pasta, ou organizar automaticamente arquivos de dados brutos em subpastas por data.

Exemplo simples de automação (macOS/Linux) — rodar um script Python direto do terminal:
```bash
python3 meu_script.py
```

Exemplo de encadeamento de comandos — criar uma pasta e já entrar nela, em uma linha só:
```bash
mkdir projeto_dados && cd projeto_dados
```
O `&&` executa o segundo comando **somente se o primeiro der certo** — é a base de como scripts de automação mais complexos são construídos.

---

Pode parecer muita coisa agora no começo sobre os terminais, mas você vai ver que no dia a dia vamos usar tranquilamente ele. Se esquecer algum comando, o que é esperado e normal, é só pesquisar o que quer fazer na internet e tentar no terminal! 
E é óbvio, você não precisa criar pastas a todos os momentos pelo terminal, os sistemas operacionais fornecem muitas coisas (como essa) de uma forma muito simples e fácil, não tem porque sofrer!