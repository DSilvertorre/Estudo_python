---
tags:
  - Code
  - Python
---
---

### Funções
Ações pré-determinadas que indicam o que irá aparecer na tela

Ex: `print("Hello world")` | a função "print" é um comando para que alguma mensagem apareça na tela para o usuário, nesse exemplo a mensagem será "Hello World"

Lista de funções: https://docs.python.org/3/library/functions.html
**Print** - Comando que indica a mensagem que deve aparecer no terminal

**Input** - Comando que além de indicar uma mensagem no terminal, garante a entrada de dados do usuário. Ex: `input("Qual o seu nome?")` | Terminal: Qual o seu nome? Danilo.
A informação Danilo é a entrada e o input é responsável por guardar e referenciar isso.

---

### Tipos de dados

**Integer**: Uso de números inteiros, positivos ou negativos. Ex: `2026`
**Float**: Uso de números decimais. Ex: `7.90`
**String**: Uso de caracteres, letras e símbolos. Ex: `"Olá, tudo bem?"`
Bool: Números Booleanos, apenas compara valores e dizem se são verdadeiros ou falsos. 
Ex: `True` or `False`
Outros tipos de dados: https://docs.python.org/3/library/stdtypes.html

---

### Variáveis, parametros e retorno de valores
**Variável é um valor que referencia a entrada de informação**. Ela necessariamente não segue uma sintaxe ou ação pré-determinada, pode ser nomeada pelo programador e diferentes tipos como valores numéricos ou texto.

Exemplo: 
`nome = input("Qual o seu nome?")`
`print("Olá ", nome)`
Terminal: 
Qual o seu nome? Danilo
Olá Danilo

**Explicação: Neste exemplo a variável será "nome", que terá o seu valor retornado na segunda linha**
Obs: Neste exemplo a variável poderia ter outra descrição além de "nome", por isso eles são diferentes das funções, elas não tem uma ação pré-determinada

---

Além do uso de print para retornar valores você pode usar "F strings" que usam o fazem referencia a alguma variável dentro de uma string.

Exemplo:
`nome = input("Qual o seu nome?")`
`print(Olá {}, tudo bem?) .format(nome))`

o comando .format é capaz de pegar a variável e referencia-lá na string utilizando apenas colchetes e o mesmo pode ser feito em sequencia com diferentes variáveis

---
A forma mais comum e complicada ao mesmo tempo de declarar variáveis é utilizando parametros. Parâmetros são as variáveis listadas entre parênteses na definição de uma função. Eles são essenciais para que as funções possam receber informações externas e trabalhar com elas
Sempre quando utilizamos um parâmetro é necessário declarar o **argumento**, ele é importante para chamar a função que deseja realizar.

Exemplo: 
`def calcular_retangulo(largura,altura):`
    `return largura * altura`

`area1 = int(input("Altura:"))`
`area2 = int(input("Largura:"))`

`resultado = calcular_retangulo(area1,area2)`

- <mark style="background: #FF5582A6;">Def é a função responsável pode declarar o argumento e os parâmetros</mark>
- <mark style="background: #FFB86CA6;">calcular_retangulo = argumento, quando utilizarmos este argumento irá chamar os parametros, como na ultima linha</mark>
- <mark style="background: #FFF3A3A6;">largura e altura = parâmetros, receberam valores assim como as variáveis atráveis do input area1 e area2</mark>

---

### Bugs
Erros que impedem a execução do código, por estarem fora do padrão exigido pela linguagem, o código não consegue ser lido pelo programa

---

### Comentários
Qualquer tipo de comentários sobre qual é a função do código, o que ele faz, como faz ou etc.... pode ser feita durante o código utilizando apenas um #

Exemplo: 
`# Quero dar um oi para todos
`print("Olá mundo")`
