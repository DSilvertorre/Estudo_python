# Declarando variáveis
def gerar_recibo(produto, desconto):
    if produto >= 500:
        desconto = 80
    elif produto >= 200:
        desconto = 90
    else: 
        desconto = 100
    return produto /100 * desconto
# aplicar desconto
valor_do_produto = float(input("Valor do produto:"))
valor_extra = 0

valor_final = gerar_recibo(valor_do_produto, valor_extra)


# Exibir na compra
print(f"Olá, a sua compra ficou no valor de {valor_final}\nAdorariamos te informar que você recebeu um desconto, o valor antes do desconto era {valor_do_produto}")
