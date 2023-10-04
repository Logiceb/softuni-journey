budget_film = float(input())
number_extras = int(input())
price_for_cloths = float(input())

amount_of_decor = budget_film * (10 / 100)
amount_of_cloths = number_extras * price_for_cloths

if number_extras > 150:
    discount = amount_of_cloths * (10 / 100)
    amount_of_cloths = amount_of_cloths - discount

total_price_for_film = amount_of_decor + amount_of_cloths

diff = abs(budget_film - total_price_for_film)

if budget_film >= total_price_for_film:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")

else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")