#Pares e impares
def is_even(x):
    return x % 2 == 0

x = int(input("Qual o valor de x?"))
if is_even(x):
    print("É par")
else:
    print("É impar")
