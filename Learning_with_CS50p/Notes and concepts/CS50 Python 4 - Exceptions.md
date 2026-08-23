## **Exceções**

Exceções são problemas que surgem durante a execução do programa: coisas que dão errado dentro do código.

```python
# Exemplo: 
print("hello, world)
```

Note que omitimos intencionalmente uma aspa.

Ao executar o código no terminal gera um erro. O interpretador reporta um erro de sintaxe. Erros de sintaxe geralmente significam que você deve verificar se digitou o código corretamente.

---

## **Erros de tempo de execução**

Erros de tempo de execução referem-se àqueles causados por comportamentos inesperados no código. Por exemplo, imagine que você esperava que o usuário digitasse um número, mas ele digitou um caractere. O programa pode gerar um erro devido a essa entrada inesperada do usuário.

```python
# Exemplo:
x = int(input("What's x?"))
print(f"x is{x}")

# Output
What's x? Olá
ValueError: invalid literal for int() with base 10: 'cat'
```

Observe que, ao incluir as chaves `f`, instruímos o Python a interpolar o conteúdo entre elas como o valor de `x`. Além disso, ao testar o código, você pode imaginar como alguém poderia facilmente digitar uma string ou um caractere em vez de um número. Mesmo assim, um usuário poderia não digitar nada — simplesmente pressionando a tecla Enter.

Como programadores, devemos adotar uma postura defensiva para garantir que nossos usuários estejam inserindo o que esperamos.

Se executarmos este programa e digitarmos “olá”, veremos `ValueError: invalid literal for int() with base 10: 'cat'`. Em outras palavras, a `int`função não consegue converter o texto “gato” em um número.

Uma estratégia eficaz para corrigir esse possível erro seria criar um sistema de "tratamento de erros" para garantir que o usuário se comporte conforme o esperado.

---

## **`try`**

Em Python , `try`  is_user_entry e `except` is_user_entry são maneiras de testar a entrada do usuário antes que algo dê errado. Modifique seu código da seguinte forma:

```python
try:
    x = int(input("What's x?"))
    print(f"x is{x}")
except ValueError:
    print("x is not an integer")
```

Observe como, ao executar este código, a entrada `50`será aceita. No entanto, digitar algo diferente `cat`exibirá uma mensagem para o usuário, explicando por que sua entrada não foi aceita.

Esta ainda não é a melhor maneira de implementar este código. Observe que estamos tentando usar apenas duas linhas de código. Para uma melhor prática, devemos usar `try`o mínimo possível de linhas de código que possam falhar.

```python
try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")

print(f"x is{x}")
```

Observe que, embora isso atinja nosso objetivo de usar o mínimo de linhas possível, agora nos deparamos com um novo erro! Nos deparamos com um `NameError` onde `x is not defined`. 

De fato, se você examinar a ordem das operações em `x = int(input("What's x?"))`, da direita para a esquerda, verá que ele pode receber um caractere inserido incorretamente e tentar atribuí-lo como um inteiro. Se isso falhar, a atribuição do valor de  `x` nunca ocorrerá. Portanto, não há nenhum x para imprimir na nossa última linha de código.

---

## **`else`**

 `Else` é outra forma de implementação `try`que pode detectar erros dessa natureza.

```python
try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is{x}")
```

Observe que, se nenhuma exceção ocorrer, o bloco de código dentro de  `else`. Ao executar o programa `python number.py`e fornecer `50`, você notará que o resultado será impresso. Tentando novamente, desta vez fornecendo  `cat`, você notará que o programa agora captura o erro.

Considere melhorar nosso código: note que estamos sendo um pouco rudes com o usuário. Se o usuário não cooperar, simplesmente encerramos o programa. Pense em como podemos usar um loop para solicitar a cooperação do usuário `x`e, caso ele não coopere, solicitá-la novamente!

```python
while True:
    try:
        x = int(input("What's x?"))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is{x}")
```

Observe que o `while True`loop será infinito. Se o usuário inserir a entrada correta, podemos sair do loop e imprimir o resultado. Agora, um usuário que inserir algo incorretamente será solicitado a inserir a entrada novamente.

---

## **Criando uma função para obter um número inteiro**

Certamente, haverá muitas situações em que desejaremos obter um número inteiro do usuário. Modifique seu código da seguinte forma:

```python
def main():
    x = get_int()
    print(f"x is{x}")

def get_int():
    while True:
        try:
            x = int(input("What's x?"))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x

main()
```

Observe que estamos manifestando muitas propriedades excelentes. Primeiro, abstraímos a capacidade de obter um número inteiro. Agora, todo este programa se resume às três primeiras linhas do programa.

Mas ainda podemos melhor isso:

```python
def main():
    x = get_int()
    print(f"x is{x}")

def get_int():
    while True:
        try:
            x = int(input("What's x?"))
        except ValueError:
            print("x is not an integer")
        else:
            return x

main()
```

Observe que isso `return`não apenas interromperá o loop, mas também retornará um valor.

Outra alternativa:

```python
def main():
    x = get_int()
    print(f"x is{x}")

def get_int():
    while True:
        try:
            return int(input("What's x?"))
        except ValueError:
            print("x is not an integer")

main()
```

Observe que isso faz a mesma coisa que a versão anterior do nosso código, só que com menos linhas.

---

## **`pass`**

Podemos fazer com que nosso código não avise o usuário, mas simplesmente repita a pergunta inicial, modificando o código da seguinte forma:

```python
def main():
    x = get_int()
    print(f"x is{x}")

def get_int():
    while True:
        try:
            return int(input("What's x?"))
        except ValueError:
            pass

main()
```

Note que nosso código ainda funcionará, mas não informará repetidamente o usuário sobre o erro. Em alguns casos, você desejará deixar bem claro para o usuário qual erro está sendo gerado. Em outras ocasiões, você pode simplesmente optar por solicitar a entrada do usuário novamente.

Um último ajuste poderia melhorar a implementação desta `get_int`função. No momento, observe que o prompt está codificado diretamente no código `get_int`. Provavelmente, queremos passar um prompt que o usuário veja quando solicitado a inserir dados. Modifique seu código da seguinte forma:

```python
def main():
    x = get_int("What's x?")
    print(f"x is{x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()

```

## `raise`

No Python, a instrução `raise` serve para **lançar ou gerar** manualmente uma exceção (um erro) no seu código. Ela é usada quando você quer interromper o programa de propósito porque alguma regra de negócio ou condição esperada não foi atendida.

**Forçar um erro:** Você define o tipo de exceção (como `ValueError`, `TypeError`, ou uma exceção customizada) e uma mensagem explicativa.

**Repassar erros (`reraise`):** Você pode usar um `raise` sozinho dentro de um bloco `except` para relançar o mesmo erro após tratá-lo ou registrá-lo. 

**Exemplo prático:**

```python 
def definir_idade(idade):
	if idade <0:
		raise ValueError('A idade não pode ser um número negativo!')
			return idade
```