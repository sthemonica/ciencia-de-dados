## Aula 1 de ambientes virtuais — o conceito + pip/venv

Quando estamos mexendo com códigos, no nosso caso usando o Python, nós podemos ter várias bibiotecas para nos auxiliar. Elas são basicamente como livros, onde podemos consultar comandos e não precisar criar do zero. Porém, cada vez que existe uma atualização, as bibliotecas tem uma nova versão (assim como o próprio Python). 

Hoje o Python está na versão 3.14, mas nem todas as bibliotecas conseguem rodar com tranquilidade nele, já que elas precisam se ajustar e lançar novas versões também. 

Agora imagina você fazendo um projeto e do ABSOLUTO NADA as coisas pararem de funcionar, ou porque foram descontinuadas ou atualizadas. Você teria um tempo muito grande de readaptação e consequentemente atrasaria entregas. Agora imagina ter vários projetos ao mesmo tempo e todos eles terem problemas de versões, e você não sabe o que aconteceu, onde arrumar... 

É quase igual quando a gente está em viagem e em algum momento a mala fica desarrumada e com todas as roupas bagunçadas, você não sabe mais quais são as roupas limpas, as roupas sujas, o que você quer usar. E a solução mais prática para isso é setorizar a mala com aqueles saquinhos de organização. Um para as meias, outro para roupas íntimas, outro para camisetas, outro para calças, e também um saquinho para roupas sujas! A setorização você faz como preferir, mas ajuda a não ter tanta bagunça.

Para fazer a setorização aqui, podemos criar **ambientes virtuais**. Eles são como os nossos sacos organizadores, mas em cada ambiente vamos ter uma versão pré-estabelecida do Python, você pode deixar as bibliotecas arrumadas para aquele projeto, pode configurar tudo do jeito que precisar para aquele momento. Quando outro projeto surgir, com outras necessidades, você cria um novo ambiente virtual. Fica muito mais fácil de encontrar os problemas de versões e resolver eles.

### Mas e como criamos um ambiente virtual?
Nós temos diversas opções de como criar ambientes virtuais e vamos explorar nesses próximos vídeos. O primeiro deles é utilizando o `pip` e `venv`. Eles estão funcionando desde que o mundo do Python é mundo e vamos entender como usar.

Para criar um ambiente, de qualquer forma que escolhermos, vamos utilizar o nosso terminal de comando. No meu caso eu estou utilizando o sistema do macOS, então os exemplos serão nesse ambiente. Não se preocupe que os comando são basicamente os mesmos, e se você precisar de ajuda é só nos procurar, tudo bem?

Para criar uma pasta, vamos usar o comando `mkdir` e depois dele colocar o nome da pasta, como nesse caso vamos usar **teste_pip**.

Depois disso vamos acessar a pasta **teste_pip** usando o comando `cd`, que é basicamente procurar dentro do seu computador.

E agora que estamos dentro dessa pasta, vamos criar um ambiente virtual usando o venv e instalar o python3.

Lista de comandos:
```
mkdir teste_pip
cd teste_pip
python3 -m venv .venv
```


Esses comandos criou uma pasta .venv com uma cópia isolada do Python. Agora para acessar nosso ambiente virtual vamos colocar o seguinte comando:

```
source .venv/bin/activate
```

Na parte esquerda do nosso terminal, na frente do caminho da nossa pasta, agora aparece um `(.venv)`, isso quer dizer que conectamos no nosso 'saquinho organizador'.

Agora posso instalar algumas bibliotecas aqui dentro. Para isso vou usar o pip, que é um gerenciador de pacotes para o Python.

```
pip install pandas
```

Vamos testar se nossa biblioteca está funcionando dentro do nosso ambiente e qual a sua versão. Vamos usar o seguinte comando:

```
python3 -c "import pandas; print(pandas.__version__)"
```

Ela está ok e retornou a versão dela! Mas vamos sair do ambiente e ver o que vai acontecer se usarmos o mesmo comando anterior.

Primeiro, para sair do ambiente, digite `deactivate` e rode essa linha da comando usando o ENTER. 
E agora tente novamente importar o pandas e depois saber sua versão.

```
python3 -c "import pandas; print(pandas.__version__)"
```

**Ué, ele sumiu???**

A resposta é não! Ele está apenas naquele nosso ambiente, no nosso saquinho organizador, na gavetinha virtual que criamos! Quando usamos o `deactivate` nós voltamos para o ambiente geral do computador, que não instalamos nenhuma biblioteca!

Conforme você for fazendo o projeto, vai sentir necessidades diferentes e vai procurar bibliotecas que podem te ajudar e para instalar pelo pip geralmente é `pip instal` + `nome_da_biblioteca`. Mas sempre que tiver dúvidas do comando correto, pode procurar no Google, por exemplo.

### E como posso fazer para instalar várias bibliotecas de uma só vez?

Podemos usar um arquivo de texto, geralmente o nome dele é `requirements.txt`. A gente pode pensar que ele é como uma super lista de compras para uma receita, do tipo _"ok, eu quero fazer um bolo de chocolate, mas quais são os ingredientes?"_

Vamos voltar para nosso ambiente .venv que criamos antes.

```
source .venv/bin/activate
```

Você pode criar a mão o seu arquivo `requirements.txt` e deixar na mesma pasta que estamos usando nosso .venv e após isso pode rodar o comando de instalar tudo ao mesmo tempo, que é:

```
pip install -r requirements.txt
```

Mas digamos que você está na outra face da moeda e quer saber quais são todas as suas bibliotecas que estão ali dentro do projeto, com todas as versões. Para isso vamos fazer os seguintes comandos:
```
pip freeze > requirements.txt
cat requirements.txt
```

Agora se formos na pasta, teremos o arquivo `requirements.txt` criado, sem esforço algum. Ele é como uma foto de tudo que está dentro do seu ambiente - e isso é o que previne aquilo de **"MAS NA MINHA MÁQUINA ESTÁ RODANDO..."**

Ou seja, ter uma lista de requerimentos base, com as bibliotecas, é o que faz o seu projeto ser reprodutível em qualquer lugar! Você cria um novo ambiente, coloca o seu arquivo de requerimentos e _voilá_, tudo está funcionando novamente da forma que você precisa, em qualquer computador!

Agora que nós já exploramos sobre o que é nosso ambiente virtual e como criar um ambiente com o `.venv` e instalar bibliotecas com o `pip`, você já consegue criar suas gavetinhas virtuais. Porém existem outros métodos que podemos explorar para criar nossas gavetinhas que são mais eficientes, e em alguns momentos até são mais recomendados. 

É como se estivessemos numa aula de marcenaria agora, o que eu acabei de ensinar é como fazer uma gaveta, mas cortando a madeira usando um serrote, nas próximas podemos usar ferramentas mais modernas e rápidas.
