product = input()
city = input()
quantity = float(input())

quantity_price = 0

if city == "Sofia":
    if product == "coffee":
        quantity_price = quantity * 0.5
    elif product == "water":
        quantity_price = quantity * 0.8
    elif product == "beer":
        quantity_price = quantity * 1.2
    elif product == "sweets":
        quantity_price = quantity * 1.45
    elif product == "peanuts":
        quantity_price = quantity * 1.6

elif city == "Plovdiv":
    if product == "coffee":
        quantity_price = quantity * 0.4
    elif product == "water":
        quantity_price = quantity * 0.7
    elif product == "beer":
        quantity_price = quantity * 1.15
    elif product == "sweets":
        quantity_price = quantity * 1.3
    elif product == "peanuts":
        quantity_price = quantity * 1.5

elif city == "Varna":
    if product == "coffee":
        quantity_price = quantity * 0.45
    elif product == "water":
        quantity_price = quantity * 0.7
    elif product == "beer":
        quantity_price = quantity * 1.10
    elif product == "sweets":
        quantity_price = quantity * 1.35
    elif product == "peanuts":
        quantity_price = quantity * 1.55

print(quantity_price)