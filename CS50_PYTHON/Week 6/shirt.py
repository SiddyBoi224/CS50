import sys
from PIL import Image,ImageOps

def change(input,output):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(input) as input:
            photo = ImageOps.fit(input, shirt.size)
            photo.paste(shirt, shirt)
            photo.save(output)
    except FileNotFoundError:
        sys.exit("Input does not exist")


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        ext = ["jpg", "jpeg", "png"]
        input = sys.argv[1].split(".")
        output = sys.argv[2].split(".")
        if output[1].lower() not in ext:
            sys.exit("Invalid Input")
        elif output[1] != input[1]:
            sys.exit("Input and output have different extensions")
        else:
            change(sys.argv[1],sys.argv[2])

if __name__=="__main__":
    main()
