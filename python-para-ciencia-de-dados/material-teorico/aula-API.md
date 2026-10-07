- O que é uma API e como funcionam as requisições

API (Application Programming Interface, ou Interface de Programação de Aplicações) é uma forma de um programa conversar com outro programa.

Quando abrimos um aplicativo de clima no celular, ele não tem um termômetro dentro dele. O aplicativo pede essas informações para um outro programa, geralmente num servidor da internet, que responde com a temperatura, a chance de chuva e tudo mais. Essa conversa entre o aplicativo e o servidor acontece através de uma API.

> Um exemplo disso é um restaurante. Você (o cliente) não entra na cozinha para preparar o seu prato. Você faz o pedido para o garçom, ele leva até a cozinha, e depois traz o prato pronto até a sua mesa.
>
> A API é o garçom: ela recebe o seu pedido, leva até o sistema que tem as informações, e traz a resposta de volta. Você não precisa saber como a cozinha funciona, só precisa saber fazer o pedido do jeito certo.

**Cliente e servidor**

Toda conversa com uma API tem dois lados:

- **Cliente**: quem faz o pedido. Pode ser um site, um aplicativo ou o nosso código Python
- **Servidor**: quem recebe o pedido, processa e devolve uma resposta

O pedido que o cliente faz se chama **requisição** (request), e o que o servidor devolve se chama **resposta** (response).

**A URL**

Toda requisição de API é feita para um endereço, a **URL**, igual aos endereços que digitamos no navegador.

```text
https://pokeapi.co/api/v2/pokemon/pikachu
```

- `https://pokeapi.co`: o endereço do servidor
- `/api/v2/pokemon/pikachu`: o caminho, chamado de **endpoint**, que diz qual informação queremos

Cada endpoint dá acesso a uma informação diferente. Trocando `pikachu` por `charmander`, por exemplo, pedimos as informações de outro pokémon.

**Os métodos**

Além do endereço, a requisição diz **o que queremos fazer** com aquela informação. Isso é o **método**:

- `GET`: buscar uma informação
- `POST`: criar uma informação nova
- `PUT`: atualizar uma informação existente
- `DELETE`: apagar uma informação

O mais comum de todos é o `GET`. Toda vez que você abre um site no navegador, ele está fazendo uma requisição `GET`.

**A resposta**

Quando o servidor responde, ele envia duas coisas principais: um **código de status** e os **dados**.

O código de status é um número que diz se deu tudo certo ou não:

- `200`: deu certo
- `201`: deu certo, e algo novo foi criado
- `400`: o pedido foi feito de forma errada
- `404`: o que você pediu não foi encontrado
- `500`: deu erro no servidor

Uma regra fácil de lembrar: códigos que começam com **2** são sucesso, com **4** o erro foi de quem pediu, e com **5** o erro foi do servidor.

Já os dados geralmente chegam no formato **JSON**, aquele mesmo que vimos no tópico de arquivos:

```json
{
    "id": 25,
    "name": "pikachu",
    "height": 4,
    "weight": 60
}
```

Como o JSON se transforma facilmente em um dicionário do Python, fica muito simples usar esses dados no nosso código.

**REST**

Você vai ouvir bastante o termo **API REST**. REST é um conjunto de regras para organizar uma API, e a maioria das APIs que usamos no dia a dia segue esse padrão.

Na prática, uma API REST é aquela que usa URLs para identificar as informações, os métodos `GET`, `POST`, `PUT` e `DELETE` para dizer o que fazer com elas, e responde geralmente em JSON. Ou seja: tudo o que vimos até aqui!

---

- Introdução a APIs REST: fazendo requisições com requests

Para fazer requisições no Python, usamos a biblioteca `requests`. Ela não vem instalada com o Python, então precisamos instalar pelo terminal:

```bash
uv add requests
```

Nos exemplos, vamos usar a **PokéAPI** (`https://pokeapi.co`), uma API gratuita com informações sobre pokémons. Ela é ótima para aprender, porque não precisa de cadastro nem de senha.

Uma dica: antes de usar uma API no código, cole a URL no navegador. Como o navegador faz uma requisição `GET`, você consegue ver o JSON que a API devolve e entender a estrutura dos dados.

**Fazendo a primeira requisição**

```python
# arquivo pokemon.py
import requests

resposta = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
print(resposta.status_code)
```

O `requests.get` faz uma requisição `GET` para a URL informada e guarda a resposta do servidor na variável `resposta`.

Com o `status_code`, vemos o código de status da resposta. Nesse caso, o resultado será `200`, ou seja, deu tudo certo.

**Lendo os dados**

```python
dados = resposta.json()
print(dados["name"])
```

O `.json()` transforma o JSON da resposta em um dicionário do Python. A partir daí, acessamos as informações como em qualquer dicionário, e o resultado será `pikachu`.

```python
print(dados["id"])
print(dados["weight"])
```

O resultado será `25` e `60`.

Atenção: cada API tem a sua própria forma de organizar os dados. Na PokéAPI, a altura vem em decímetros e o peso em hectogramas, então o Pikachu tem 0,4 metros e 6 kg. Por isso, é sempre importante ler a documentação da API que estamos usando.

**Acessando dados dentro de dados**

Nem toda informação está no primeiro nível do JSON. Os tipos do pokémon, por exemplo, vêm em uma lista de dicionários:

```json
"types": [
    {
        "slot": 1,
        "type": {
            "name": "electric",
            "url": "https://pokeapi.co/api/v2/type/13/"
        }
    }
]
```

Para chegar no nome do tipo, precisamos percorrer a lista e entrar em cada dicionário:

```python
for item in dados["types"]:
    print(item["type"]["name"])
```

O resultado será `electric`. Para pokémons com dois tipos, como o Charizard, os dois seriam mostrados.

```python
imagem = dados["sprites"]["front_default"]
print(imagem)
```

A PokéAPI também envia o link da imagem do pokémon. Abrindo esse link no navegador, vemos a figura do Pikachu.

**Quando o pokémon não existe**

```python
resposta = requests.get("https://pokeapi.co/api/v2/pokemon/amendoim")
print(resposta.status_code)
```

Como o pokémon `amendoim` não existe, o resultado será `404`.

Nesse caso, a resposta não tem um JSON com os dados, e tentar usar o `.json()` vai gerar um erro. Por isso, sempre verificamos o status antes de usar os dados:

```python
if resposta.status_code == 200:
    dados = resposta.json()
    print(dados["name"])
else:
    print("Pokémon não encontrado")
```

**Enviando parâmetros**

Algumas APIs aceitam **parâmetros**, que são informações extras para filtrar ou limitar a resposta. Eles aparecem na URL depois de um `?`:

```text
https://pokeapi.co/api/v2/pokemon?limit=5&offset=0
```

- `limit=5`: quantos pokémons queremos receber
- `offset=0`: a partir de qual posição começar (igual no array, começamos no valor 0)

Em vez de montar a URL na mão, podemos passar os parâmetros como um dicionário, e o `requests` monta a URL para nós:

```python
parametros = {"limit": 5, "offset": 0}
resposta = requests.get("https://pokeapi.co/api/v2/pokemon", params=parametros)
```

```python
for pokemon in resposta.json()["results"]:
    print(pokemon["name"])
```

Nesse endpoint, a lista de pokémons vem dentro da chave `results`. O resultado será os 5 primeiros pokémons: `bulbasaur`, `ivysaur`, `venusaur`, `charmander` e `charmeleon`.

Mudando o `offset` para `5`, recebemos os 5 seguintes. Isso se chama **paginação**, e é muito comum em APIs que têm muitos dados.

**Juntando tudo**

Agora, vamos criar um pequeno programa onde o usuário digita o nome de um pokémon e recebe as informações dele:

```python
# arquivo pokedex.py
import requests

nome = input("Digite o nome de um pokémon: ").lower()
url = f"https://pokeapi.co/api/v2/pokemon/{nome}"
```

O `.lower()` transforma o texto em letras minúsculas, porque a PokéAPI só reconhece os nomes assim. Se o usuário digitar `Pikachu`, enviamos `pikachu`.

```python
try:
    resposta = requests.get(url, timeout=10)
except requests.exceptions.RequestException:
    print("Não foi possível conectar à API")
    raise SystemExit
```

Aqui usamos o que vimos no tópico de tratamento de erros. Se a internet cair ou a API estiver fora do ar, a requisição gera um erro, e o bloco `except` mostra uma mensagem em vez de quebrar o programa.

O `timeout=10` define que vamos esperar no máximo 10 segundos pela resposta. Sem ele, o programa poderia ficar travado esperando para sempre.

```python
if resposta.status_code == 200:
    dados = resposta.json()
    tipos = [item["type"]["name"] for item in dados["types"]]
```

Se o pokémon foi encontrado, pegamos os dados e montamos uma lista só com o nome dos tipos.

```python
    print(f"Nome: {dados['name']}")
    print(f"Tipos: {', '.join(tipos)}")
else:
    print("Pokémon não encontrado")
```

O `', '.join(tipos)` junta os itens da lista em um texto só, separados por vírgula. Para o Charizard, por exemplo, o resultado será `Tipos: fire, flying`.

**Criando dados com POST**

A PokéAPI só permite buscar informações, então para testar o `POST` vamos usar o **JSONPlaceholder** (`https://jsonplaceholder.typicode.com`), uma API feita justamente para praticar.

```python
# arquivo criar_post.py
import requests

novo_post = {"title": "Meu primeiro post", "body": "Aprendendo APIs com Python", "userId": 1}
resposta = requests.post("https://jsonplaceholder.typicode.com/posts", json=novo_post)
```

O `requests.post` envia uma requisição `POST`. Com o `json=novo_post`, o dicionário é convertido para JSON e enviado junto com a requisição.

```python
print(resposta.status_code)
print(resposta.json())
```

O resultado será `201`, que indica que algo novo foi criado, e o JSON do post com um `id` gerado pelo servidor.

Como o JSONPlaceholder é uma API de testes, o post não é salvo de verdade, mas a resposta é exatamente igual à de uma API real.

**Resumindo**

- `requests.get(url)`: busca informações
- `requests.post(url, json=dados)`: envia informações novas
- `resposta.status_code`: mostra se a requisição deu certo
- `resposta.json()`: transforma a resposta em dicionário
- `params=`: envia parâmetros na URL
- `timeout=`: limita o tempo de espera pela resposta