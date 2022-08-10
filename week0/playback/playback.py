
text = input("")
playback = ""

for i in text:  # ender every index of char
    if i == " ":
        playback += "..."
    else:
        playback += i

print(playback)