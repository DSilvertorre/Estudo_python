def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
    clean = float(dollars.replace("$",""))
    return clean


def percent_to_float(percent):
    decimal = float(percent.replace('%', '')) / 100
    return decimal


main()