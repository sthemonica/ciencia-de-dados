# Aula 4 — Gráficos com Matplotlib

Depois de analisar os dados com NumPy e Pandas, o próximo passo é **mostrar** o resultado. Um gráfico deixa claro, em segundos, o que uma tabela de números levaria minutos para explicar.

O Matplotlib é a biblioteca de gráficos mais usada em Python. Para instalar:

```bash
uv add matplotlib
```

Dentro dele, usamos o módulo `pyplot`, que por convenção recebe o apelido `plt`:

```python
import matplotlib.pyplot as plt
```

**Gráfico de linha**

O gráfico de linha é ideal para mostrar como um valor muda ao longo do tempo:

```python
# arquivo grafico_linha.py
import matplotlib.pyplot as plt
import numpy as np

dias = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
temperaturas = np.array([18, 21, 19, 25, 23, 17, 20])

plt.plot(dias, temperaturas, marker="o")
plt.title("Temperatura da semana")
plt.xlabel("Dia")
plt.ylabel("Temperatura (°C)")
plt.show()
```

- `plt.plot(x, y)`: desenha a linha, com os valores de `x` no eixo horizontal e de `y` no vertical
- `marker="o"`: coloca uma bolinha em cada ponto
- `plt.title`, `plt.xlabel` e `plt.ylabel`: título do gráfico e nome de cada eixo
- `plt.show()`: abre uma janela com o gráfico

Todo gráfico deve ter título e nome nos eixos. Sem isso, quem olha não sabe o que está vendo!

**Gráfico de barras**

O gráfico de barras é ideal para comparar categorias. Vamos usar o resultado do `groupby` da aula anterior:

```python
# arquivo grafico_barras.py
import matplotlib.pyplot as plt
import pandas as pd

tabela = pd.read_csv("pessoas.csv")
media_por_cidade = tabela.groupby("cidade")["idade"].mean()

plt.bar(media_por_cidade.index, media_por_cidade.values)
plt.title("Idade média por cidade")
plt.xlabel("Cidade")
plt.ylabel("Idade média")
plt.show()
```

O `index` da Series são os nomes das cidades, e o `values` são as médias. Cada cidade vira uma barra.

**Histograma**

O histograma mostra como os valores estão **distribuídos**: quantos estão em cada faixa.

```python
plt.hist(tabela["idade"], bins=4)
plt.title("Distribuição das idades")
plt.xlabel("Idade")
plt.ylabel("Quantidade de pessoas")
plt.show()
```

O `bins=4` define em quantas faixas os valores serão divididos. Com mais dados, vale testar valores diferentes para ver qual mostra melhor a distribuição.

**Gráfico de dispersão**

O gráfico de dispersão mostra a relação entre duas variáveis numéricas. Cada ponto é um registro:

```python
horas_estudo = np.array([1, 2, 3, 4, 5, 6])
notas = np.array([4, 5, 5, 7, 8, 9])

plt.scatter(horas_estudo, notas)
plt.title("Horas de estudo x nota")
plt.xlabel("Horas de estudo")
plt.ylabel("Nota")
plt.show()
```

Aqui conseguimos ver que, quanto mais horas de estudo, maior tende a ser a nota.

**Qual gráfico usar?**

- **Linha**: evolução ao longo do tempo
- **Barras**: comparar categorias
- **Histograma**: ver como os valores se distribuem
- **Dispersão**: ver a relação entre duas variáveis

**Atalho do Pandas**

O Pandas tem uma forma curta de gerar gráficos, usando o Matplotlib por baixo dos panos:

```python
media_por_cidade.plot(kind="bar", title="Idade média por cidade")
plt.show()
```

O `kind` define o tipo: `"line"`, `"bar"`, `"hist"`, entre outros. Para explorar os dados rapidamente, esse atalho é muito prático.

**Salvando o gráfico**

Para salvar o gráfico como imagem, usamos o `savefig` **antes** do `show`:

```python
plt.savefig("temperatura.png")
plt.show()
```

Se o `savefig` vier depois do `show`, a imagem pode ser salva em branco, porque o `show` "limpa" o gráfico ao fechar a janela.

**Resumo**

- O Matplotlib é usado com `import matplotlib.pyplot as plt`
- `plot`, `bar`, `hist` e `scatter` criam gráficos de linha, barras, histograma e dispersão
- Todo gráfico precisa de título e nome nos eixos
- O Pandas tem o atalho `.plot(kind=...)`
- `savefig` salva o gráfico como imagem, sempre antes do `show`
