budget = int(input())
season = input()
number_of_fishermen = int(input())

price = 0

if season == "Spring":
    rent_for_ship = 3000
    if number_of_fishermen <= 6:
        discount = rent_for_ship * 0.10
        price = rent_for_ship - discount

    elif 7 <= number_of_fishermen <= 11:
        discount = rent_for_ship * 0.15
        price = rent_for_ship - discount

    elif number_of_fishermen >= 12:
        discount = rent_for_ship * 0.25
        price = rent_for_ship - discount

elif season == "Summer" or season == "Autumn":
    rent_for_ship = 4200
    if number_of_fishermen <= 6:
        discount = rent_for_ship * 0.10
        price = rent_for_ship - discount

    elif 7 <= number_of_fishermen <= 11:
        discount = rent_for_ship * 0.15
        price = rent_for_ship - discount

    elif number_of_fishermen >= 12:
        discount = rent_for_ship * 0.25
        price = rent_for_ship - discount

elif season == "Winter":
    rent_for_ship = 2600
    if number_of_fishermen <= 6:
        discount = rent_for_ship * 0.10
        price = rent_for_ship - discount

    elif 7 <= number_of_fishermen <= 11:
        discount = rent_for_ship * 0.15
        price = rent_for_ship - discount

    elif number_of_fishermen >= 12:
        discount = rent_for_ship * 0.25
        price = rent_for_ship - discount

if number_of_fishermen % 2 == 0 and season != "Autumn":
    discount = price * 0.05
    price = price - discount

budget_diff = abs(budget - price)

if price <= budget:
    print(f"Yes! You have {budget_diff:.2f} leva left.")

else:
    print(f"Not enough money! You need {budget_diff:.2f} leva.")