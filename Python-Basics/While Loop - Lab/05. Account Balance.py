total_money = 0
total_increased = 0

while True:
    money_withdraw = input()
    total_increased = float(money_withdraw)

    if money_withdraw <= 0:
        print("Invalid operation!")
        print(f"Total: {total_money:.2f}")

    if money_withdraw == "NoMoreMoney":
        print(f"Total: {total_money:.2f}")

    print(f"Increase: {total_increased:.2f}")

