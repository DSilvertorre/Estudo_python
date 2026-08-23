lista_de_compras = []

def main():
    while True:
        try:
            compras = input('')
            lista_de_compras.append(compras)
        except (EOFError, KeyboardInterrupt):     
                    join = ", ".join(lista_de_compras)
                    treated = join.replace(", ", "\n")
                    count_objects()
                    break

def count_objects():
    
    contagem = {}
    for item in lista_de_compras:
            if item in contagem:
                contagem[item] += 1
            else: contagem[item] = 1

    for item, quantidade in contagem.items():
          print(f"{quantidade} {item}".upper())
    return contagem

main()