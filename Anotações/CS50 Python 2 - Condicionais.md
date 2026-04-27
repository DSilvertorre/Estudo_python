---
tags:
  - Code
  - Python
---
---

### IF, ELIF e ELSE
São blocos de código que controlam o fluxo do programa com base em condições.

- **if (se):** Inicia a condição. Executa o código se a condição for **verdadeira**.
- **elif (senão se):** Abreviação de "else if". Verifica uma nova condição caso o `if` anterior seja **falso**. Você pode ter vários.
- **else (senão):** O "plano B". Executa se **nenhuma** das condições anteriores forem verdadeiras

---
### Operadores lógicos
Usados para combinar ou inverter condições (sempre retornam `True` ou `False`).

- **`and` (e):** Retorna `True` apenas se **todas** as condições forem verdadeiras.
- **`or` (ou):** Retorna `True` se pelo menos **uma** das condições for verdadeira.
- **`not` (não):** Inverte o valor booleano (o que é `True` vira `False` e vice-versa).

---
### Match
Ele compara um objeto com múltiplos casos, permitindo extrair valores e validar estruturas complexas de forma mais legível que `if/elif/else`
`comando = "sair"`

`match comando:`
    `case "entrar":`
        `print("Bem-vindo!")`
    `case "sair":`
        `print("Até logo!")`
    `case _:`
        `print("Comando desconhecido") # O "_" funciona como o else do match`

