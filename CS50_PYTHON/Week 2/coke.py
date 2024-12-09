def main():
    amount = 50
    accept = [5,10,25]

    while amount > 0:
        print(f"Amount Due: {amount}")
        insert = int(input("Insert Coin: "))
        if insert in accept:
            amount -= insert
        if amount < 0:
            break

    print("Change Owed:",abs(amount))


if __name__ == "__main__":
    main()
