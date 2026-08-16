#Exercicio: Criar um algoritmo que verifica se é possivel o usuario 
# continuar apostando ou passou do limite de créditos, nessa suposição podemos dizer que ele 
# possui 1000 reais de créditos para gastar em fichas. A função do algoritmo é subtrair valores
# até que usuário não tenha mais créditos para gastar e envie uma mensagem de alerta

# Objetivo: Praticar o uso de while looping, testando funções como break e operações como += ou -=

credito = 1000
while credito >=0:
    fichas = int(input("Quanto você deseja apostar? "))

# Se o usuário não deseja mais apostar, basta digitar "0"
    if fichas == 0:
        print(f"\n Sessão finalizada. Você saiu com R$ {credito} ")
        break

# Subtrai os créditos a cada valor apostado
    credito -= fichas
    if credito <= 0:
        print("\n Seus créditos acabaram! Faça um novo depósito para continuar.")