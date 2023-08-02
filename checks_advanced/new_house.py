type_flower = input()
count_flower = int(input())
budget = int(input())

flower_price = 0

if type_flower == "Roses":
    flower_price = count_flower * 5
    if count_flower > 80:
        flower_price = flower_price - (flower_price * 0.1)
    else:
        flower_price = flower_price

elif type_flower == "Dahlias":
    flower_price = count_flower * 3.8
    if count_flower > 90:
        flower_price = flower_price - (flower_price * 0.15)
    else:
        flower_price = flower_price

elif type_flower == "Tulips":
    flower_price = count_flower * 2.8
    if count_flower > 80:
        flower_price = flower_price - (flower_price * 0.15)
    else:
        flower_price = flower_price

elif type_flower == "Narcissus":
    flower_price = count_flower * 3
    if count_flower < 120:
        flower_price = flower_price * 1.15
    else:
        flower_price = flower_price

elif type_flower == "Gladiolus":
    flower_price = count_flower * 2.5
    if count_flower < 80:
        flower_price = flower_price * 1.2
    else:
        flower_price = flower_price

price_diff = abs(budget - flower_price)
if budget >= flower_price:
    print(f"Hey, you have a great garden with {count_flower} {type_flower} and {price_diff:.2f} leva left.")

else:
    print(f"Not enough money, you need {price_diff:.2f} leva more.")