def valor_final():
    valor_soma = int(input("Valor do produto:"))
    if valor_soma >=100:
        desconto = 15
        return valor_soma - desconto
    elif valor_soma >=20:
        desconto = 10
        return valor_soma - desconto
    
    else: 
        valor_soma <=20
    return valor_soma - desconto + 10

resultado = valor_final()
print(resultado)
                         
