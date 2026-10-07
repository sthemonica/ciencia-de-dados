# Capstone Fraude — Aula 5: README do projeto

## O README do projeto 

### O que é o README e por que ele importa

O `README.md` é o arquivo que o GitHub mostra **logo abaixo da lista de arquivos**, na página principal do repositório. Para quem visita o seu projeto (um recrutador, um colega), ele é a **vitrine**: muitas pessoas vão ler só o README, sem abrir nenhum notebook.

Um bom README responde, nesta ordem:

1. O que é este projeto?
2. Que problema ele resolve?
3. Com quais dados?
4. O que foi feito, passo a passo?
5. O que foi descoberto?
6. Como eu rodo na minha máquina?

### Markdown essencial

O `.md` no nome significa **Markdown**, um jeito simples de formatar texto. É o mesmo formato das células de texto dos notebooks.

| Você escreve | Vira |
|---|---|
| `# Título` | título principal |
| `## Seção` | título de seção |
| `**negrito**` | **negrito** |
| `- item` | item de lista |
| ```codigo``` | `codigo` (trecho de código no meio do texto) |
| `[texto](https://link.com)` | um link |
| `![descrição](imagens/grafico.png)` | uma imagem |
| três crases + `bash` ... três crases | um bloco de código |
| linhas com `\|` separando colunas | uma tabela |

Para imagens, o caminho é **a partir do README**. Como o README fica na raiz do projeto e as imagens na pasta `imagens`, o caminho é `imagens/nome.png`.

### A estrutura do README

| Seção | O que colocar |
|---|---|
| **Título e resumo** | o nome do projeto e uma frase dizendo o que ele faz |
| **Contexto** | o problema de negócio: por que detectar fraude importa |
| **Dados** | de onde vieram, tamanho e as duas bases geradas |
| **Estrutura do projeto** | as pastas e os notebooks, na ordem |
| **Etapas** | o que foi feito em cada notebook, do carregamento às análises |
| **Principais descobertas** | as conclusões, com os gráficos |
| **Como executar** | os comandos para rodar o projeto do zero |
| **Próximos passos** | o que ainda vai ser feito |
| **Tecnologias e autor** | as bibliotecas usadas e o seu contato |

### Exemplo de README completo

Use este exemplo como base. Os trechos entre colchetes, como `[Seu nome]`, são para você preencher.

````markdown
# Detecção de Fraude em Compras Online

Análise exploratória de 150 mil compras online para entender o que diferencia uma compra fraudulenta de uma legítima.

## Contexto

Fraudes em compras online geram prejuízo direto para as lojas, com estornos e produtos perdidos. A loja já usa um modelo que dá um score de fraude para cada compra, mas ele ainda confunde muitas compras legítimas com fraudes.

Este projeto investiga os dados das compras para responder: **o que muda entre compras legítimas e fraudes?**

## Dados

- [Origem dos dados]
- 150.000 compras, depois da remoção de 250 linhas duplicadas
- 5% das compras são fraude (base desbalanceada)

Depois da limpeza, os dados foram separados em duas bases, ligadas pela coluna `id_compra`:

| Base | Conteúdo |
|---|---|
| `dados_compra.csv` | data, hora, dia da semana, valor, país, produto, documentos entregues e a marcação de fraude |
| `fraude_scores.csv` | os 10 scores de fraude, o score do modelo atual e a marcação de fraude |

## Estrutura do projeto

```text
├── data/
│   ├── raw/                  # dados originais
│   └── processed/            # dados unificados, limpos e separados
├── imagens/                  # gráficos usados neste README
├── notebooks/
│   ├── 01_carregamento.ipynb
│   ├── 02_limpeza.ipynb
│   ├── 03_analise_univariada.ipynb
│   ├── 04_analise_bivariada.ipynb
├── pyproject.toml
└── uv.lock
```

## Etapas

### 1. Carregamento

[Descrever como os arquivos originais foram carregados e unificados em uma única base.]

### 2. Limpeza e preparação

| Problema | Decisão |
|---|---|
| 250 linhas duplicadas (exportadas duas vezes) | removidas |
| Data lida como texto | convertida para data |
| País ausente em 194 compras | preenchido com "Desconhecido" |
| Scores com até 8,66% de ausentes | preenchidos com a mediana de cada score |
| Documento 2 ausente em 72,57% das compras | preenchidos como não entregue |
| Documentos em formatos diferentes (`1`/`0` e `Y`/`N`) | padronizados para `1`/`0` |

Também foram criadas novas colunas: países agrupados (BR, AR e Outros), hora da compra e dia da semana.

### 3. Análise univariada

Distribuição de cada variável: o valor das compras é assimétrico, com mediana de R$ 20 e média de R$ 43, puxada por poucas compras muito caras.

### 4. Análise bivariada

Comparação de cada variável entre compras legítimas e fraudes.

## Principais descobertas

**1. Quem não entrega nenhum documento frauda muito mais:** 16% de fraude, contra 4% de quem entrega.

![Taxa de fraude por entrega de documento](imagens/taxa_fraude_documento.png)

**2. O Brasil tem a maior taxa de fraude:** 5,5%, contra 3,7% da Argentina e 2,5% dos outros países.

![Taxa de fraude por país](imagens/taxa_fraude_pais.png)

**3. A madrugada concentra as fraudes:** em vários dias, a taxa passa de 15% nesse horário.

![Taxa de fraude por dia e hora](imagens/fraude_dia_hora.png)

**4. As fraudes custam um pouco mais**, com mediana de R$ 26 contra R$ 20, mas com bastante sobreposição.

![Valor da compra por classe](imagens/valor_por_classe.png)

**5. Nenhum score sozinho explica a fraude:** a maior correlação, a do score do modelo atual, é de apenas 0,17. A fraude aparece na combinação de vários sinais.

## Como executar

Pré-requisito: ter o [uv](https://docs.astral.sh/uv/) instalado.

```bash
git clone [link do repositório]
cd [nome da pasta]
uv sync
```

O `uv sync` instala todas as bibliotecas nas versões usadas no projeto. Depois, abra os notebooks da pasta `notebooks/` na ordem, do `01` ao `05`.

## Próximos passos

- [ ] Treinar um modelo de classificação usando as variáveis mais promissoras
- [ ] Comparar o novo modelo com o score do modelo atual

## Tecnologias

Python, Pandas, NumPy, Matplotlib, Seaborn, Plotly e uv.

## Autor

[Seu nome] · [LinkedIn] · [GitHub]
````

### Dicas finais

- **Escreva para quem não conhece o projeto.** Leia o README como se fosse a primeira vez: dá para entender sem abrir nenhum notebook?
- **Números convencem.** "Fraudes são mais frequentes sem documento" é vago; "16% contra 4%" é concreto.
- **Uma frase antes de cada gráfico.** O leitor deve saber o que procurar na imagem antes de olhar para ela.
- **Mantenha atualizado.** A cada nova etapa do projeto, atualize o README.

## Salvando no GitHub

```bash
git add .
git commit -m "Adiciona visualizações finais e README"
git push
```

Depois do push, abra o repositório no GitHub e confira se o README aparece na página inicial e se as imagens carregam.
