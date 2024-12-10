import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r'<iframe[^>]*src="https?://(?:www\.)?(?:youtube\.com/embed/|youtube\.com/watch\?v=|youtu\.be/)([\w-]+)', s)

    if match:
        video = match.group(1)
        return f"https://youtu.be/{video}"
    else:
        return None

if __name__ == "__main__":
    main()
