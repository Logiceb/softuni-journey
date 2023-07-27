budget_film = float(input())
number_statist = int(input())
price_cloths = float(input())

sum_decor = budget_film * 0.1
sum_cloths = number_statist * price_cloths

if number_statist > 150:
    sum_cloths = sum_cloths - (sum_cloths * 0.1)

total_sum = sum_decor + sum_cloths

diff = abs(budget_film - total_sum)
if total_sum <= budget_film:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")

else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")