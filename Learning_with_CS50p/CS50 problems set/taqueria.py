menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

sum_list = []

def main():
    while True:
        try:
            ask = input("Item: ").strip().title()
            values = menu[ask]
            for foods, values in menu.items():
                if ask == foods:
                    suma(values)

        except (EOFError, KeyboardInterrupt):
            print("\nPedido finalizado!")
            break
        except Exception:
            continue

def suma(ask):
    sum_list.append(ask)
    q = sum(sum_list)
    print(f"${q:.2f}").strip()
main()