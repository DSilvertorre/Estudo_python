def valor_final(produto,frete, desconto):
    if produto >=100:
        frete = 0
        desconto = 15
        return produto + frete - desconto
    elif produto >=20:
        frete = 0
        desconto = 0
        return produto + frete - desconto
    else: 
        pass
    return produto + frete - desconto

valor_soma = int(input("Valor do produto:"))
valor_extra = 10
desconto_add = 0

resultado = valor_final(valor_soma, valor_extra, desconto_add)
print(resultado)
                         
