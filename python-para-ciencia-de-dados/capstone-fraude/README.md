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