
text = input("Input: ").strip()

print("Ouput: ", end = "")

for i in text:
    test = i.lower()
    if not (test == 'a' or test == 'e' or test == 'i' or test == 'o' or test == 'u'): #vowel
        print(i, end = "")

print()
exit()