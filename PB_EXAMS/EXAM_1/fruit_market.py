price_strawberries = float(input())
amount_bananas = float(input())
amount_oranges = float(input())
amount_raspberries = float(input())
amount_strawberries = float(input())

price_raspberries = price_strawberries - 0.5 * price_strawberries
price_oranges = price_raspberries - (0.4 * price_raspberries)
price_bananas = price_raspberries - (0.8 * price_raspberries)

sum_raspberries = amount_raspberries * price_raspberries
sum_oranges = amount_oranges * price_oranges
sum_bananas = price_bananas * amount_bananas
sum_strawberries = amount_strawberries * price_strawberries

total_price = sum_raspberries + sum_oranges + sum_bananas + sum_strawberries

print(f"{total_price:.2f}")
