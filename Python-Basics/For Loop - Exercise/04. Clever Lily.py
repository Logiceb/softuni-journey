age_lily = int(input())
price_for_washing_machine = float(input())
unit_price_per_toy = int(input())

total_money = 0
total_toys = 0
current_money = 0

for age in range(1, age_lily + 1):
    if age % 2 == 0:
        current_money += 10
        total_money += current_money - 1

    else:
        total_toys += 1

total_money += total_toys * unit_price_per_toy
diff = abs(total_money - price_for_washing_machine)

if total_money >= price_for_washing_machine:
    print(f"Yes! {diff:.2f}")

else:
    print(f"No! {diff:.2f}")

