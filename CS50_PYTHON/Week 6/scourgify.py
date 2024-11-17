import csv,sys

def clean(infile,outfile):
    try:
        with open(infile, "r") as file, open(outfile, "w") as output:
            reader = csv.DictReader(file)
            writer = csv.DictWriter(output, fieldnames = ["first", "last", "house"])
            writer.writeheader()
            for line in reader:
                last, first = line["name"].split(", ")
                house = line["house"]
                writer.writerow({"first": first, "last":last, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {infile}")



def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:] == ".csv" and sys.argv[2][-4:] == ".csv":
            print(clean(sys.argv[1],sys.argv[2]))
        else:
            sys.exit("Not a CSV file")


if __name__=="__main__":
    main()
