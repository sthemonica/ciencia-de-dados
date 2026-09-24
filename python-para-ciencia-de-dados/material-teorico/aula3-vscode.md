# VS Code para Ciência de Dados

## Por que deixar o Google Colab

O Google Colab é um ótimo aliado para aprender Python: é fácil de usar, permite criar células de Jupyter, subir um dataset e rodar código sem precisar configurar nada — o ambiente já vem pronto.

O problema aparece quando o projeto precisa **escalar**. Nesse ponto, o Colab passa a exigir mais cuidado:
- É preciso vincular o projeto ao Google Drive e reservar espaço de armazenamento
- O tempo de processamento gratuito é limitado — projetos maiores exigem uma conta paga (upgrade)
- Sempre que a sessão expira, é necessário rodar todo o código de novo e recarregar os dados — o que se torna inviável à medida que o projeto cresce

### Quando usar cada um

- **Google Colab**: ótimo para tarefas rápidas, sem necessidade de configurar ambiente, ou para compartilhar código rapidamente com outras pessoas
- **VS Code**: melhor opção quando o projeto precisa de um ambiente mais robusto, configurado especificamente para as necessidades daquele projeto, rodando localmente

> Existem outras interfaces populares, como o **PyCharm** — a escolha final depende do que você se sente mais confortável usando. Este material segue com VS Code por conta das extensões úteis para ciência de dados e pela integração facilitada com Markdown, csv e GitHub.

---

## Conhecendo a interface do VS Code

Ao abrir o VS Code pela primeira vez, você vê a tela de **boas-vindas (Welcome)**, com opções para criar um novo arquivo, abrir uma pasta, ou clonar um repositório do GitHub.

### A barra lateral esquerda

A barra lateral concentra os principais recursos do editor:

1. **Explorer** — mostra as pastas e arquivos do seu projeto. É aqui que você abre uma pasta existente, clona um repositório ou cria uma nova pasta no sistema.

2. **Search** — funciona como um "Ctrl+F" para todo o projeto: busca um termo dentro de todos os arquivos abertos, útil quando você tem vários datasets (CSV) e códigos e precisa lembrar onde algo está. Também permite fazer busca e substituição (search & replace).

3. **Source Control (o ícone de "ramo")** — voltado para o controle de versão com Git/GitHub. É aqui que você conecta seu repositório e gerencia commits. Funciona com qualquer sistema de versionamento, mas o GitHub é o mais usado na comunidade de dados, inclusive para exibir portfólio.

4. **Run and Debug** — voltado para encontrar erros ao rodar o código, mais indicado para códigos automatizados/scripts. Para o dia a dia de ciência de dados trabalhando em Jupyter Notebook, esse recurso é usado com menos frequência.

5. **Extensions** — a área mais importante para configurar o ambiente de trabalho (detalhada abaixo).

Se você ainda não tem esses ícones, está tudo bem. Conforme vamos colocando extensões no nosso ambiente, algumas figurinhas a mais aparecem.

---

## Extensões essenciais

### Python

A extensão oficial de Python permite que o VS Code **leia e execute código Python** — ela não instala o Python no seu computador, isso é feito separadamente (será abordado em outra aula sobre configuração de ambiente).

> Ao instalar extensões de desenvolvedores independentes (não a Microsoft, criadora do VS Code), o editor pergunta se você confia no autor antes de prosseguir ("Trust Publisher and Install"). Extensões populares já foram verificadas por muitos usuários, mas o critério de confiança é sempre seu.

Uma extensão complementar recomendada é a de **indentação do Python** — ajuda a manter a estrutura de indentação correta, algo essencial em Python, já que a linguagem usa indentação para definir blocos de código (como uma "escadinha").

### Jupyter

Fornecida pela Microsoft, essa extensão recria a experiência de células que você já conhece do Google Colab — com blocos de código e blocos de texto (Markdown) dentro do próprio VS Code.

> É possível alternar para uma versão "pré-lançamento" da extensão, mas isso significa aceitar recursos ainda em desenvolvimento, com maior chance de bugs.

---

## Personalizando o VS Code

### Temas de cores

Digitando "Theme" na barra de comandos, você acessa diversas opções de tema visual — desde temas escuros a claros, passando por opções bem conhecidas como:
- **GitHub Theme** (Dark, incluindo versão para daltonismo)
- **Dracula Official** — tema roxo bastante popular, com variações "soft" (mais escura) e "inteira" (mais roxa)
- **Bearded Theme** — oferece uma grande variedade de paletas de cores (azulados, amarronzados, tons pastéis como "blueberry", "raspberry", "menta")

A escolha do tema é inteiramente pessoal — não existe um tema "certo". Há até uma brincadeira comum na comunidade de programação de que temas claros "chamam mais bugs" que os escuros, mas isso não passa de humor, não uma regra técnica.

### Ícones de arquivo

Para deixar a navegação mais intuitiva visualmente, é possível instalar pacotes de ícones customizados (ex: "Data Pack Icons", com visual inspirado em jogos como Minecraft, ou temas com ícones de gatinhos como "Moca", "Latte", "Frappé"). Isso substitui os ícones padrão de pastas e arquivos por versões mais estilizadas, sem afetar a funcionalidade.

### Formatação de arquivos específicos

- **Rainbow CSV** — colore diferentes colunas de um arquivo `.csv` com cores distintas, facilitando a leitura de datasets com muitas colunas separadas por vírgula
- **Markdown All in One** — auxilia na escrita de arquivos `.md`, usados tanto nas células de texto do Jupyter Notebook quanto para documentar projetos (por exemplo, um bom README no GitHub)

### Outras

- **Auto Docstring** — ajuda a gerar documentação (docstrings) para funções em Python, explicando o que cada função faz
- **Claude Code** — permite conversar com uma IA diretamente na lateral do editor, pedindo ajuda ou revisão de código
- **GitLens** — facilita o trabalho com Git dentro do editor
- **Portuguese Language Pack** — traduz a interface do VS Code para português, para quem tem menos familiaridade com inglês
- **Prettier** — formatador automático de código, ajudando a manter um padrão consistente de escrita

---

## Contas e sincronização

Fazer login com uma conta (por exemplo, GitHub) dentro do VS Code permite **sincronizar configurações** entre computadores diferentes — temas, extensões instaladas e preferências ficam salvos e podem ser recuperados automaticamente ao trocar de máquina, sem precisar reconfigurar tudo do zero (opção "Sync Settings").

---

## Por que o VS Code compensa no longo prazo

Resumindo os ganhos práticos em relação ao Google Colab:
- O ambiente roda **localmente**, sem depender de sessões que expiram
- Não há necessidade de recarregar dados e rerodar tudo por causa de limite de sessão
- Você tem controle total do ambiente: Python, bibliotecas e configurações específicas para cada projeto
- Integração facilitada com GitHub, permitindo manter o histórico de versões e compartilhar código com uma equipe de forma organizada

A partir desse ponto, as próximas aulas passam a usar o VS Code como ambiente principal de trabalho, incluindo a configuração de ambientes virtuais e instalação de bibliotecas.