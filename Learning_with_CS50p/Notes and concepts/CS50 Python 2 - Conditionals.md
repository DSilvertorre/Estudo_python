# CS50 Python - Aula 2: Condicionais

## 1. IF, ELIF e ELSE

São blocos de código que controlam o fluxo do programa com base em condições.

### Componentes:

- **`if` (se):** Inicia a condição. Executa o código se a condição for **verdadeira**.
- **`elif` (senão se):** Abreviação de "else if". Verifica uma nova condição caso o `if` anterior seja **falso**. Você pode ter vários.
- **`else` (senão):** O "plano B". Executa se **nenhuma** das condições anteriores forem verdadeiras.

### Exemplo:

```python
idade = int(input("Qual a sua idade? "))
if idade >= 18:
    print("ok, pode acessar")
elif idade < 18:
    print("ainda é muito jovem, tente novamente mais tarde")
else:
    print("Error!")
```

**Saída esperada:**
```
Qual a sua idade? 25
ok, pode acessar
```

### Explicação:
- Se `idade >= 18`, a primeira condição é verdadeira e o código dentro do `if` é executado
- Se a primeira condição for falsa, verifica o `elif`
- Se nenhuma das condições anteriores for verdadeira, executa o `else`

---

## 2. Operadores de Comparação

Usados para comparar valores e retornam `True` ou `False`:

- `==` → Igual a
- `!=` → Diferente de
- `>` → Maior que
- `<` → Menor que
- `>=` → Maior ou igual a
- `<=` → Menor ou igual a

### Exemplo:

```python
nota = int(input("Qual foi sua nota? "))

if nota >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")
```

---

## 3. Operadores Lógicos

Usados para combinar ou inverter condições. Sempre retornam `True` ou `False`.

### `and` (e):

Retorna `True` apenas se **todas** as condições forem verdadeiras.

```python
idade = int(input("Qual sua idade? "))
carteira = input("Possui carteira de motorista? (sim/não) ")

if idade >= 18 and carteira == "sim":
    print("Pode dirigir!")
else:
    print("Não pode dirigir!")
```

**Saída esperada:**
```
Qual sua idade? 20
Possui carteira de motorista? (sim/não) sim
Pode dirigir!
```

---

### `or` (ou):

Retorna `True` se pelo menos **uma** das condições for verdadeira.

```python
dia_semana = input("Que dia é hoje? ")

if dia_semana == "sábado" or dia_semana == "domingo":
    print("É fim de semana!")
else:
    print("É dia de semana!")
```

**Saída esperada:**
```
Que dia é hoje? sábado
É fim de semana!
```

---

### `not` (não):

Inverte o valor booleano (o que é `True` vira `False` e vice-versa).

```python
ehchovendo = True

if not ehchovendo:
    print("Vou sair de casa")
else:
    print("Fico em casa")
```

**Saída esperada:**
```
Fico em casa
```

---

## 4. Match (Python 3.10+)

A instrução `match` é uma alternativa mais moderna e legível ao `if/elif/else` para comparar um valor com múltiplos casos.

### Sintaxe:

```python
match variavel:
    case valor1:
        # código executado se variavel == valor1
    case valor2:
        # código executado se variavel == valor2
    case _:
        # código padrão (como "else")
```

### Exemplo:

```python
opcao = input("Escolha uma opção (1, 2 ou 3): ")

match opcao:
    case "1":
        print("Você escolheu a opção 1")
    case "2":
        print("Você escolheu a opção 2")
    case "3":
        print("Você escolheu a opção 3")
    case _:
        print("Opção inválida!")
```

**Saída esperada:**
```
Escolha uma opção (1, 2 ou 3): 2
Você escolheu a opção 2
```

### Vantagens do Match:

- Mais legível que múltiplos `elif`
- Mais eficiente para muitas comparações
- Suporta padrões mais complexos
- O `case _` atua como o `else` padrão

---

## 5. Ordem de Prioridade de Operadores Lógicos

Quando combinamos múltiplos operadores, a ordem de execução é:

1. `not` (maior prioridade)
2. `and`
3. `or` (menor prioridade)

### Exemplo:

```python
# Sem parênteses - segue a ordem de prioridade
resultado = True or False and False  # Resultado: True

# Com parênteses - deixa explícito
resultado = (True or False) and False  # Resultado: False
```

**Dica:** Use parênteses para deixar o código mais claro e evitar erros!

---

## 6. Boas Práticas

- ✓ Use parênteses para deixar a lógica clara
- ✓ Indente corretamente o código dentro dos blocos
- ✓ Use nomes descritivos para variáveis
- ✓ Evite condições muito complexas (divida em variáveis intermediárias)
- ✓ Prefira `match` para múltiplas comparações do mesmo valor
- ✓ Mantenha o código legível e fácil de entender

### Exemplo de Bom Código:

```python
idade = int(input("Qual é sua idade? "))
tem_carteira = input("Tem carteira de motorista? (sim/não) ").lower() == "sim"
eh_sobrio = input("Está sóbrio? (sim/não) ").lower() == "sim"

if idade >= 18 and tem_carteira and eh_sobrio:
    print("Pode dirigir com segurança!")
else:
    print("Não pode dirigir!")
```
