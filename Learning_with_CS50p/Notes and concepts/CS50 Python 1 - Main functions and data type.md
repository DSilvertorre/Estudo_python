# CS50 Python - Aula 1: Funções e Tipos de Dados

## 1. Funções Pré-determinadas

Aplicação dentro da linguagem de programação ou biblioteca que faz uma ação já determinada, sem precisar criar uma lógica ou chamá-la dentro do programa.

### Exemplo de Função Básica:

```python
# A função "print" é um comando para que alguma mensagem apareça na tela para o usuário
# Neste exemplo, a mensagem será "Hello World"

print("Hello World")
```

**Referência:**
- [Documentação de funções built-in](https://docs.python.org/3/library/functions.html)

---

## 2. Tipos de Dados

### **Integer**
Números inteiros, positivos ou negativos.

Exemplo: `2026`, `-42`, `0`

### **Float**
Números decimais.

Exemplo: `7.90`, `3.14`, `-2.5`

### **String**
Caracteres, letras e símbolos entre aspas.

Exemplo: `"Olá, tudo bem?"`, `'João'`, `"123"`

### **Boolean**
Valores Booleanos que indicam se algo é verdadeiro ou falso.

Exemplo: `True`, `False`

**Referência:**
- [Documentação sobre tipos de dados](https://docs.python.org/3/library/stdtypes.html)

---

## 3. Variáveis, Parâmetros e Retorno de Valores

### O que é uma Variável?

Uma variável é um espaço de armazenamento que guarda um valor. Diferentemente das funções, as variáveis não possuem uma ação pré-determinada - elas simplesmente armazenam dados. Uma variável pode ser nomeada pelo programador e armazenar diferentes tipos de valores: numéricos, texto, booleanos, etc.

### Exemplo Básico:

```python
nome = input("Qual é o seu nome? ")
print("Olá", nome)
```

**Saída esperada:**
```
Qual é o seu nome? João
Olá João
```

### Explicação:
- A variável `nome` recebe o valor fornecido pelo usuário através da função `input()`
- O nome de uma variável pode ser qualquer descrição (não precisa ser necessariamente "nome")
- Variáveis são diferentes de funções porque apenas armazenam valores, não realizam ações

### Formatação de Strings com f-strings:

O método de f-string é a forma moderna e recomendada de inserir variáveis dentro de uma string, utilizando chaves `{}`:

```python
nome = input("Qual é o seu nome? ")
print(f"Olá, {nome}! Tudo bem?")
```

**Alternativa com .format():**
```python
nome = input("Qual é o seu nome? ")
print("Olá, {}! Tudo bem?".format(nome))
```

---

## 4. Operadores Matemáticos

Assim como na matemática, podemos realizar operações com a linguagem Python usando operadores simples: adição (`+`), subtração (`-`), multiplicação (`*`) e divisão (`/`). Essas operações funcionam com integers, floats e variáveis.

### Operadores Disponíveis:
- `+` → Adição
- `-` → Subtração
- `*` → Multiplicação
- `/` → Divisão (resultado é float)
- `//` → Divisão inteira
- `%` → Resto da divisão (módulo)
- `**` → Exponenciação

### Exemplo:

```python
ano_atual = int(input("Em que ano estamos? "))
ano_nascimento = int(input("Qual ano você nasceu? "))
idade = ano_atual - ano_nascimento
print(f"Você tem {idade} anos")
```

---

## 5. Definir Funções

### O que é uma Função?

A forma mais comum e eficiente de reutilizar código é através de funções. As funções recebem **parâmetros** (variáveis listadas entre parênteses na definição) para processar informações externas e trabalhar com elas.

### Componentes:

- **`def`** → Palavra-chave responsável por declarar uma função
- **Parâmetros** → Variáveis que a função recebe entre parênteses
- **Argumento** → O valor passado quando a função é chamada
- **`return`** → Retorna um valor ao chamar a função

### Exemplo:

```python
def calcular_retangulo(largura, altura):
    return largura * altura

area1 = int(input("Altura: "))
area2 = int(input("Largura: "))

resultado = calcular_retangulo(area1, area2)
print(f"A área é: {resultado}")
```

### Explicação dos Elementos:

- **`def`** → Palavra-chave para declarar a função
- **`calcular_retangulo`** → Nome da função (argumento), quando chamada, executa os parâmetros
- **`largura` e `altura`** → Parâmetros, recebem os valores `area1` e `area2` do input
- **`return`** → Retorna o resultado da multiplicação

---

## 6. Bugs

**O que é um bug?**

Erros que impedem a execução correta do código. Bugs ocorrem quando o código está fora do padrão exigido pela linguagem, impedindo que o programa seja lido e executado corretamente.

### Exemplos de bugs comuns:
- Falta de `:` após definição de função
- Indentação incorreta
- Parênteses desbalanceados
- Nomes de variáveis não definidas
- Tipos de dados incompatíveis

---

## 7. Comentários

Comentários são anotações no código que explicam a função, a lógica ou as operações realizadas. Em Python, comentários são iniciados com `#`.

### Exemplo:

```python
# Este é um comentário explicativo
# Eu quero dar oi ao mundo

print("Olá mundo")  # Este comentário está na mesma linha do código
```

### Comentários em Múltiplas Linhas:

```python
"""
Este é um comentário em múltiplas linhas
Pode ser usado para documentar funções
ou explicar trechos maiores de código
"""
```

**Notas:**
- Comentários são ignorados pelo Python e não afetam a execução do código
- Use comentários para documentar sua lógica e facilitar o entendimento por outros programadores
- Evite comentários óbvios; prefira explicar o "por quê" em vez do "o quê"
