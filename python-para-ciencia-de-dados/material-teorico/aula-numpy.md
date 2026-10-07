# Aula 2 — NumPy e arrays

Na aula anterior usamos bibliotecas que já vêm com o Python. A partir de agora, vamos usar bibliotecas **externas**, que precisam ser instaladas. Elas são a base da ciência de dados em Python.

**Instalando bibliotecas com o uv**

Para instalar bibliotecas externas, vamos usar o `uv`, o gerenciador do nosso projeto. Ele baixa a biblioteca da internet e deixa pronta para importar. Para instalar o NumPy, rodamos no terminal, dentro da pasta do projeto:

```bash
uv add numpy
```

O `uv add` instala a biblioteca e também anota no arquivo `pyproject.toml` que o projeto depende dela. Assim, qualquer pessoa que baixar o projeto consegue instalar as mesmas bibliotecas.

Depois de instalado, ele é importado como qualquer outro módulo. A única diferença é que precisamos instalar uma vez antes.

> Se aparecer o erro `ModuleNotFoundError: No module named 'numpy'`, significa que a biblioteca ainda não foi instalada.

**O que é o NumPy?**

O NumPy (Numerical Python) é uma biblioteca para trabalhar com números de forma rápida. Ele é tão importante que o Pandas e o Matplotlib, que veremos nas próximas aulas, são construídos em cima dele.

O coração do NumPy é o **array**: uma sequência de valores, parecida com uma lista, mas feita para fazer contas.

```python
# arquivo exemplo_numpy.py
import numpy as np

temperaturas = np.array([18, 21, 19, 25, 23, 17, 20])
print(temperaturas)
```

O resultado será:

```text
[18 21 19 25 23 17 20]
```

Assim como o `pd` do Pandas, o `np` é o apelido que toda a comunidade usa para o NumPy.

**Array x lista**

À primeira vista, o array parece uma lista. A grande diferença aparece quando fazemos contas:

```python
lista = [1, 2, 3]
print(lista + [10, 20, 30])

array = np.array([1, 2, 3])
print(array + np.array([10, 20, 30]))
```

O resultado será:

```text
[1, 2, 3, 10, 20, 30]
[11 22 33]
```

Com listas, o `+` **junta** as duas. Com arrays, o `+` **soma** elemento por elemento.

E não precisamos de um `for` para fazer uma conta em todos os valores. Por exemplo, para converter as temperaturas de Celsius para Fahrenheit:

```python
fahrenheit = temperaturas * 9 / 5 + 32
print(fahrenheit)
```

O resultado será:

```text
[64.4 69.8 66.2 77.  73.4 62.6 68. ]
```

A conta é aplicada em cada elemento de uma vez. Com uma lista, precisaríamos percorrer valor por valor com um `for`.

Outra diferença: um array guarda valores de **um único tipo**. Se misturarmos inteiros e decimais, o NumPy converte todos para decimal:

```python
print(np.array([1, 2.5, 3]))
```

O resultado será `[1.  2.5 3. ]`. Podemos ver o tipo dos valores com `temperaturas.dtype`, que nesse caso mostra `int64` (números inteiros).

**Acessando valores**

O acesso por posição funciona igual ao das listas:

```python
print(temperaturas[0])
print(temperaturas[-1])
print(temperaturas[1:4])
```

O resultado será `18`, `20` e `[21 19 25]`.

**Estatísticas rápidas**

O array já vem com funções para resumir os dados:

```python
print(temperaturas.mean())
print(temperaturas.max())
print(temperaturas.min())
print(temperaturas.sum())
print(temperaturas.std())
```

- `mean()`: média
- `max()` e `min()`: maior e menor valor
- `sum()`: soma de todos os valores
- `std()`: desvio padrão, que mostra o quanto os valores se espalham em torno da média

**Filtrando com condições**

Ao comparar um array com um valor, recebemos um array de `True` e `False`:

```python
print(temperaturas > 20)
```

O resultado será:

```text
[False  True False  True  True False False]
```

E podemos usar esse resultado para filtrar apenas os valores que atendem à condição:

```python
dias_quentes = temperaturas[temperaturas > 20]
print(dias_quentes)
```

O resultado será `[21 25 23]`.

Guarde bem essa forma de filtrar, porque ela vai aparecer de novo no Pandas!

**Arrays com duas dimensões**

Um array também pode ter linhas e colunas, como uma tabela de números (uma **matriz**). Por exemplo, as notas de dois alunos em três provas:

```python
notas = np.array([
    [7, 8, 6],
    [9, 5, 10]
])

print(notas.shape)
print(notas[1, 2])
```

- `shape`: mostra o formato do array, no caso `(2, 3)`, ou seja, 2 linhas e 3 colunas
- `notas[1, 2]`: acessa a linha 1, coluna 2, que é o valor `10`

Também podemos calcular a média por linha ou por coluna com o `axis`:

```python
print(notas.mean(axis=1))
print(notas.mean(axis=0))
```

- `axis=1`: calcula ao longo das colunas, ou seja, a média de cada **aluno**: `[7. 8.]`
- `axis=0`: calcula ao longo das linhas, ou seja, a média de cada **prova**: `[8.  6.5 8. ]`

**Criando arrays prontos**

O NumPy tem funções para criar arrays sem digitar valor por valor:

```python
print(np.zeros(3))
print(np.arange(0, 10, 2))
print(np.linspace(0, 1, 5))
```

O resultado será:

```text
[0. 0. 0.]
[0 2 4 6 8]
[0.   0.25 0.5  0.75 1.  ]
```

- `np.zeros(3)`: array com 3 zeros
- `np.arange(0, 10, 2)`: parecido com o `range`, de 0 até 10 (sem incluir), de 2 em 2
- `np.linspace(0, 1, 5)`: 5 valores igualmente espaçados entre 0 e 1

**Resumo**

- Bibliotecas externas são instaladas com `uv add`
- O array é como uma lista feita para contas: as operações são aplicadas em todos os elementos de uma vez
- Arrays têm funções prontas como `mean`, `max`, `min`, `sum` e `std`
- Podemos filtrar com condições, como `temperaturas[temperaturas > 20]`
- Arrays podem ter duas dimensões, e o `shape` mostra o formato
