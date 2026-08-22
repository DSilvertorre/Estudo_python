def main():
    greetings = input("Greetings: ").strip().capitalize()
    if greetings.startswith("Hello"):
        print("$0")
    elif greetings.startswith("H"):
        print("$20")
    else: print("$100")

main ()