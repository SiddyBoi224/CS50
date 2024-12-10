import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    regex = r"(0?[1-9]|1[0-2]):?([0-5][0-9])? (AM|PM)"
    check = re.search(r"^" + regex + r" to " + regex + r"$", s)
    if check:
        from_time = change(check.group(1), check.group(2), check.group(3))
        to_time = change(check.group(4), check.group(5), check.group(6))
        return f"{from_time} to {to_time}"
    else:
        raise ValueError("Invalid time format")

def change(hh, mm, x):

    if hh == "12":
        hour = "00" if x == "AM" else "12"
    else:
        hour = f"{int(hh):02}" if x == "AM" else f"{int(hh) + 12:02}"

    minute = "00" if mm is None else f"{int(mm):02}"
    return f"{hour}:{minute}"

if __name__ == "__main__":
    main()
