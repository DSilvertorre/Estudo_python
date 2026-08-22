def main():
    camel = input("camelCase: ")
    add_snake_case = []

    for l in camel:
        if l.isupper():
            add_snake_case.append(f"_{l.lower()}")
        else:
            add_snake_case.append(l)

    snake_case = ''.join(add_snake_case)
    print(f"snake_case: {snake_case}")

main()
