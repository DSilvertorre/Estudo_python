def main():
    interpreter = input("Expressions: ").split(" ")
    x, y, z = (interpreter)

    x = float(x)
    z = float(z)

    if y == "+":
        print(x + z)
    elif y == "-":
        print(x - z)
    elif y == "*":
        print(x * z)
    elif y == "/":
        print(x / z)
    else: print("Não encontrado")

main()