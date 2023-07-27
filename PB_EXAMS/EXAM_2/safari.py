budget = float(input())
liters = float(input())
day_week = input()

price_fuel = liters * 2.10
total_guide = price_fuel + 100

if day_week == "Sunday":
    total_guide = total_guide - (total_guide * 0.2)

elif day_week == "Saturday":
    total_guide = total_guide - (total_guide * 0.1)

diff = abs(budget - total_guide)
if budget > total_guide:
    print(f"Safari time! Money left: {diff:.2f} lv. ")

else:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")