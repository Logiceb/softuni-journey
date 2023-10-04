necessary_amount_of_nail = int(input())
required_amount_of_paint = int(input())
amount_of_thinner = int(input())
hours = int(input())

# · Предпазен найлон - 1.50 лв. за кв. метър
# · Боя - 14.50 лв. за литър
# · Разредител за боя - 5.00 лв. за литър

price_nylon = (necessary_amount_of_nail + 2) * 1.50
price_paint = (required_amount_of_paint + (required_amount_of_paint * (10 / 100))) * 14.50
price_thinner = amount_of_thinner * 5.00
price_bags = 0.40

total_price_for_materials = price_nylon + price_paint + price_thinner + price_bags
price_masters = (total_price_for_materials * 0.3) * hours
total_price = total_price_for_materials + price_masters

print(total_price)