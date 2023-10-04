budget = float(input())
category = input()
number_of_people = int(input())

price = 0
price_for_ticket = 0

if category == "VIP":
    price_for_ticket = 499.99 * number_of_people
    if 1 <= number_of_people <= 4:
        price = budget - budget * 0.75

    elif 5 <= number_of_people <= 9:
        price = budget - budget * 0.60

    elif 10 <= number_of_people <= 24:
        price = budget / 2

    elif 25 <= number_of_people <= 49:
        price = budget - budget * 0.40

    elif number_of_people >= 50:
        price = budget - budget * 0.25


elif category == "Normal":
    price_for_ticket = 249.99 * number_of_people
    if 1 <= number_of_people <= 4:
        price = budget - budget * 0.75

    elif 5 <= number_of_people <= 9:
        price = budget - budget * 0.60

    elif 10 <= number_of_people <= 24:
        price = budget / 2

    elif 25 <= number_of_people <= 49:
        price = budget - budget * 0.40

    elif number_of_people >= 50:
        price = budget - budget * 0.25

price_diff = abs(price - price_for_ticket)

if price_for_ticket <= price:
    print(f"Yes! You have {price_diff:.2f} leva left.")

else:
    print(f"Not enough money! You need {price_diff:.2f} leva.")
