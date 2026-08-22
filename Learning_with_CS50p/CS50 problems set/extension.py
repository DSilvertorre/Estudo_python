def main():
    image = input("File name: ").strip().lower()
    if image.endswith("gif"):
        print("image/gif")
    elif image.endswith("jpeg"):
        print("image/jpeg")
    elif image.endswith("pdf"):
        print("application/pdf")
    elif image.endswith("txt"):
        print("text/plain")
    elif image.endswith("zip"):
        print("application/zip")
    elif image.endswith("jpg"):
        print("image/jpeg")
    elif image.endswith("png"):
        print("image/png")
    else: print("application/octet-stream")

main()