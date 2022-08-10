def main():
    cost = 50

    while cost > 0:
        print(f"Amount Due: {cost}")
        give = get(cost)
        cost -= give

    print(f"Change Owed: {-cost}")

def get(cost):
    while True:
        money = int(input("Insert Coin: "))   # 30 cents don't allow run again again to be correct like 25 10, 5
        if money == 25 or money == 10 or money == 5:
            break
        else:
            print(f"Amount Due: {cost}")

    return money

if __name__ == "__main__":
    main()