
camelCase = input("camelCase: ").strip()

for i in camelCase:   
    if i.isupper():
        camelCase = camelCase[:camelCase.index(i)] + "_" + camelCase[camelCase.index(i):]

camelCase = camelCase.lower()

print(f"snake_case: {camelCase}")