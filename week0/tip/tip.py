
def main():
    dollars = dollars_to_float(input("How much was the meal? "))   # string
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")   


def dollars_to_float(d):   # $50.0
    d = d.replace("$","")
    dollars = float(d)
    return dollars  #float

def percent_to_float(p):   #string   %50
    # TODO
    p = int(p.replace("%",""))
    return float(p/100)   

main()