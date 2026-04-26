def comprimentar(nome, saudar="Olá, {}! Tudo bem?"):
    return saudar.format(nome)
print(comprimentar("Danilo"))