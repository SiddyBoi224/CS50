def main():
    num = input("Expression: ").split(" ")
    num1 = float(num[0])
    num2 = float(num[2])
    s = num[1]

    if s == "+":
        print(num1 + num2)
    elif s == "-":
        print(num1 - num2)
    elif s == "*":
        print(num1 * num2)
    elif s == "/":
        print(num1 / num2)


if __name__ == "__main__":
    main()
