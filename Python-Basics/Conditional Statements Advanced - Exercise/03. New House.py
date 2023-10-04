flower_type = input()
amount_of_flowers = int(input())
budget = int(input())

flower_price = 0

if flower_type == "Roses":
    flower_price = amount_of_flowers * 5
    if amount_of_flowers > 80:
        discount = flower_price - (flower_price * 0.10)
        flower_price = discount
    else:
        flower_price = flower_price

elif flower_type == "Dahlias":
    flower_price = amount_of_flowers * 3.8
    if amount_of_flowers > 90:
        discount = flower_price - (flower_price * 0.15)
        flower_price = discount
    else:
        flower_price = flower_price

elif flower_type == "Tulips":
    flower_price = amount_of_flowers * 2.8
    if amount_of_flowers > 80:
        discount = flower_price - (flower_price * 0.15)
        flower_price = discount
    else:
        flower_price = flower_price

elif flower_type == "Narcissus":
    flower_price = amount_of_flowers * 3
    if amount_of_flowers < 120:
        discount = flower_price + (flower_price * 0.15)
        flower_price = discount
    else:
        flower_price = flower_price

elif flower_type == "Gladiolus":
    flower_price = amount_of_flowers * 2.5
    if amount_of_flowers < 80:
        discount = flower_price + (flower_price * 0.20)
        flower_price = discount
    else:
        flower_price = flower_price

budget_diff = abs(budget - flower_price)

if flower_price <= budget:
    print(f"Hey, you have a great garden with {amount_of_flowers} {flower_type} and {budget_diff:.2f} leva left.")

else:
    print(f"Not enough money, you need {budget_diff:.2f} leva more.")
