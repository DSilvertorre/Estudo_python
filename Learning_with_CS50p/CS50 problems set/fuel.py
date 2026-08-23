def main():
    while True:
        fuel = input("Fraction: ")
        try:
            result = transform_fraction(fuel)
            if result >= 99:
                print("F")
            elif result <= 1:
                print("E")
            else: print(f"{result}%")
            break
        except (ValueError, ZeroDivisionError):
            continue


def transform_fraction(fuel):
    part = fuel.replace(",",".").split("/")
    if int(part[0]) > int(part[1]):
        raise ValueError
    if int(part[0]) < 0:
        raise ValueError
    if int(part[1]) < 0:
        raise ValueError
    x = (int(part[0]) / int(part[1]) * 100)
    return round(x)

main()