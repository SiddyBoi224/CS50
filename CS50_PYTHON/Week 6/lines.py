import sys

def count(filename):
    try:
        num = 0
        with open(filename, "r") as file:
            for line in file:
                if not(line.lstrip().startswith("#") or line.lstrip() == ""):
                    num += 1
            return num
    except FileNotFoundError:
        sys.exit("File does not exist")


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-3:] == ".py":
            print(count(sys.argv[1]))
        else:
            sys.exit("Not a Python file")


if __name__=="__main__":
    main()
