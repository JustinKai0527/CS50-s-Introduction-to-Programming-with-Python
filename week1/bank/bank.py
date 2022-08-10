
text = input("Greeting: ").strip().lower()

#if text have " " in the seperate
    # text = text[:text.index(" ")]

if "hello" in text:
    print("$0")
elif text[0] == "h":
    print("$20")
else:
    print("$100")