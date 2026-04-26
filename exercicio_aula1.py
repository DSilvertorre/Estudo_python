# Declarar variáveis
def exibir_cadastro(nome, idade):
    return f"Nome: {nome}, Idade: {idade}"
# Entrada de dados
nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
altura = float(input("Digite sua altura:"))

# Condições
if idade >= 18:
        print(f"Olá {nome}, você é maior de idade.")
else:
        print(f"Olá {nome}, lamentamos informar que você não pode participar por ter apenas {idade} anos, volte mais tarde \n quando se tornar maior de idade")