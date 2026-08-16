# Exercicio: Criar um algoritmo que calcule o valor do produto final contando com descontos e frete.
# Os comandos serão, valor da compra acima de 100, aplique um desconto de 15 reais
# Valor da compra entre 90-20, aplique um desconto de 10 reais
# Valor da compra abaixo de 20 reais, adicione o frete de 5 reais
#Respectivamente.

# Objetivo do exercicio:
# Praticar o uso de parâmetros, condicionais e operadores matemáticos
# De preferencia de uma forma lógica e código limpo

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
    return valor_soma - desconto + 5

resultado = valor_final()
print(resultado)