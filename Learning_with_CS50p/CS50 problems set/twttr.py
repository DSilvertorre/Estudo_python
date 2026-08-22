list = ["a", "e", "i", "o", "u","A","E","I","O","U"]

def main():
    a = input("Input: ").strip()

    for letra in list:
        a = a.replace(letra, "")
    print(a)
main()
