def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    if not (2 <= len(s) <= 6 and s.isalnum()):
        return False
    if s.isalpha():
        return True
    if not s[:2].isalpha():
        return False
    for i, char in enumerate(s):
        if char.isdigit():
            if char == '0':
                return False
            if not s[i:].isdigit():
                return False
            return True
    return False

if __name__ == "__main__":
    main()
