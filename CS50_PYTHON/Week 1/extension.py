def main():
    image = ["gif","png"]
    doc = ["pdf","zip"]
    ftype = input("File name: ").lower().strip().split(".")
    if ftype[-1] == "jpg" or ftype[-1] == "jpeg":
        print("image/jpeg")
    elif ftype[-1] == "txt":
        print("text/plain")
    elif ftype[-1] in image:
        print(f"image/{ftype[-1]}")
    elif ftype[-1] in doc:
        print(f"application/{ftype[-1]}")
    else:
        print("application/octet-stream")


if __name__ == "__main__":
    main()
