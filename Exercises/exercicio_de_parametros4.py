# Declarando parametros
def calcular_carrinho(nome, preço, quantidade, cupom=1):
    return preço * quantidade
# Criando dicionário
produto = {"Nome do produto": "Teclado", 
    "Preço": "28.99",
    "Quantidade": "1"
}

nome_do_produto = input("Qual produto o cliente deseja?")
print(produto)