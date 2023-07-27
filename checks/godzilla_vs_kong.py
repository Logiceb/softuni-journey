budget_film = float(input())
number_statist = int(input())
price_cloths = float(input())

price_decor = (10 * budget_film) / 100
sum_cloths = number_statist * price_cloths

if number_statist > 150:
    sum_cloths = sum_cloths - (sum_cloths * 0.1)

total_sum = price_decor + sum_cloths

money_left = abs(budget_film - total_sum)

if total_sum <= budget_film:
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")

elif total_sum > budget_film:
    print("Not enough money!")
    print(f"Wingard needs {money_left:.2f} leva more.")