# Exercicio: Criar um algoritmo que calcule o valor 
# do produto de acordo com o valor, quanto maior o valor
# da compra maior será o desconto. 
# Os valores devem ser +500, 500-200 e -200
# Os descontos devem ser 20%, 10% e 0%
#Respectivamente.

# Objetivo do exercicio:
# Praticar o uso de parâmetros, condicionais e operadores matemáticos
# De preferencia de uma forma lógica e código limpo

# Declarando parâmetros e condicionais
def gerar_recibo():
    valor = float(input("Valor do produto:"))
    if valor >= 500:
        final = valor * 0.8
    elif valor >= 200:
        final = valor * 0.9
    else:
        final = valor
        print("Compre outros produtos para receber descontos")
    return final
# Aplicar desconto
resultado = gerar_recibo()
# Exibir na compra
print(f"A sua compra ficou no valor de {resultado}\nAdorariamos te informar que você recebeu um desconto")

# Mudanças: CleanCode; Codigo sem argumentos, com apenas um retorno e poucas variáveis.