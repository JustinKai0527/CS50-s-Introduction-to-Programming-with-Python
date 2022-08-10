
text = input("File name: ").strip().lower()

if "." not in text:
    print("application/octet-stream")
    exit()

match(text[text.rindex("."):]):
    case ".gif":
        print("image/gif")
    case ".jpg":
        print("image/jpeg")
    case ".jpeg":
        print("image/jpeg")
    case ".png":
        print("image/png")
    case ".pdf":
        print("application/pdf")
    case ".txt":
        print("text/plain")
    case ".zip":
        print("application/zip")
    case _:
        print("application/octet-stream")