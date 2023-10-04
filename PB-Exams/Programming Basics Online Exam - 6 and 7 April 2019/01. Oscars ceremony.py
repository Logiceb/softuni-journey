rent_hall = int(input())

# Статуетки  – цената им е 30% по-малка от наема на залата
# Кетъринг – цената му е 15% по-малка от тази на статуетките
# Озвучаване – цената му е 1 / 2 от цената за кетъринг

price_one = rent_hall - (rent_hall * 0.3)
price_two = price_one - (price_one * 0.15)
price_three = price_two / 2

total_price = rent_hall + price_one + price_two + price_three

print(f"{total_price:.2f}")
