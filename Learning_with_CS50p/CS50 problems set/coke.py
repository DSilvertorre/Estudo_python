def main():
    valid_coins = [25, 10, 5]
    amount_due = 50

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))
        for vc in valid_coins:
            if coin == vc:
                amount_due -= coin
    change_owed = abs(amount_due)
    print(f"Change Owed: {change_owed}")

if __name__ == "__main__":
    main()

