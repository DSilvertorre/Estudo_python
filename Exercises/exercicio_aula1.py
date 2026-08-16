# Exercicio: Verificar a idade de um usuário ao se cadastrar no sistema, 
# pergunte qual é o nome e a idade do usuário e retorne no final no programa se o
# acesso dele está liberado ou não.
# 
# Objetivo: Praticar funções como variáveis, condições e funções como input e print
# 
#  Declarar variáveis
def exibir_cadastro(nome, idade):
    return f"Nome: {nome}, Idade: {idade}"
# Entrada de dados
nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))

# Condições
if idade >= 18:
        print(f"Olá {nome}, você é maior de idade.")
else:
        print(f"Olá {nome}, lamentamos informar que você não pode participar por ter apenas {idade} anos, volte mais tarde \n quando se tornar maior de idade")