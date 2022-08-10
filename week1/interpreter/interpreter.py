
x = list()

text = input("Expression: ").strip()  #white space 

x = text.split(" ")         # split give user the list 

x[0] = float(x[0])  #x

x[2] = float(x[2])  #z

match(x[1]):   #y
    case "+":
        print(x[0] + x[2])
    case "-":
        print(x[0] - x[2])
    case "/":
        print(x[0] / x[2])
    case "*":
        print(x[0] * x[2])
    case "%":
        print(x[0] % x[2])