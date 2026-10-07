## 1. Qual gráfico usar

| Gráfico | Pergunta que responde | Dados típicos | Cuidados / evite quando | Biblioteca recomendada |
|---|---|---|---|---|
| **Bar** (barras) | Como categorias se comparam? | 1 categórica + 1 numérica (ou contagem) | Eixo Y deve começar no zero. Com muitas categorias, use barras horizontais e ordene. | **seaborn** (`sns.barplot` já agrega média + IC; `sns.countplot` para contagens) |
| **Line** (linha) | Como algo evolui ao longo do tempo/ordem? | X ordenado (datas, etapas) + Y numérico | Não use com X categórico sem ordem: a linha sugere continuidade que não existe. | **matplotlib/pandas** (`df.plot()`) para séries simples; **plotly** (`px.line`) se a série for longa e o zoom ajudar |
| **Scatter** (dispersão) | Existe relação entre duas variáveis numéricas? | 2 numéricas (+ cor/tamanho para uma 3ª) | Muitos pontos se sobrepõem: use `alpha`, amostragem ou `hexbin`. **Correlação não é causalidade.** | **seaborn** (`sns.scatterplot`, `sns.regplot` com reta); **plotly** quando o hover para identificar pontos importantes |
| **Heatmap** | Como uma matriz de valores se distribui? Quais variáveis se correlacionam? | Matriz: `df.corr()`, tabela cruzada, dia × hora | Para correlação, use paleta divergente centrada em 0 (`cmap="coolwarm", center=0`). Matrizes grandes ficam ilegíveis com `annot=True`. | **seaborn** (`sns.heatmap`) |
| **Boxplot** | Como a distribuição varia entre grupos? Há outliers? | 1 categórica + 1 numérica | Esconde a forma da distribuição (bimodalidade some). Público leigo costuma não saber ler quartis. | **seaborn** (`sns.boxplot`) |
| **Violin** | Mesma pergunta do boxplot, mas mostrando a forma da distribuição | 1 categórica + 1 numérica, amostras médias/grandes | Com poucos dados a curva suavizada engana: sobreponha os pontos (`sns.stripplot`) ou use `inner="quartile"`. | **seaborn** (`sns.violinplot`, `split=True` para comparar 2 subgrupos) |
| **Histograma** | Como uma variável numérica se distribui? | 1 numérica | O número de bins muda a leitura; teste alguns valores. | **seaborn** (`sns.histplot(kde=True)`) |


## 2. Qual biblioteca escolher

| Biblioteca | Use quando | Pontos fortes | 
|---|---|---|
| **pandas `.plot()`** | Exploração rápida, "só quero ver" | Uma linha de código direto do DataFrame 
| **matplotlib** | Controle total, figura para artigo/relatório estático, gráficos fora do padrão | Base de tudo; customiza cada detalhe; exporta PNG/PDF/SVG 
| **seaborn** | Análise exploratória e estatística com DataFrames | Agrega e calcula IC sozinho; `hue`, `col`, `row` facilitam comparar grupos; visual bonito por padrão 
| **plotly (express)** | Interatividade: hover, zoom, filtros; dashboards (Dash/Streamlit); apresentar em notebook ou web | Sintaxe parecida com seaborn (`px.scatter(df, x=, y=, color=)`); interativo sem esforço 

## 3. Regra de bolso

| Objetivo | Gráfico |
|---|---|
| Comparar categorias | Bar |
| Mudança no tempo | Line |
| Relação entre duas numéricas | Scatter |
| Distribuição de uma variável | Histograma |
| Distribuição entre grupos | Boxplot (resumo) ou Violin (forma) |
| Matriz / correlação | Heatmap |

