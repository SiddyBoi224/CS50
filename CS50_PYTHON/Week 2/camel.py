def main():
    cam = input("camelCase: ")
    print("snake_case: ", end="")
    for c in cam:
        if c.islower():
            print(c, end="")
        if c.isupper():
            print("_", c.lower(), end="", sep="")
    print("\n")

if __name__ == "__main__":
    main()
