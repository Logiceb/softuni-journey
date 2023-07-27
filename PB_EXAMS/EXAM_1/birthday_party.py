hall_rent = float(input())

price_cake = hall_rent * (20 / 100)
price_drink = price_cake - ((45 / 100) * price_cake)
price_animator = hall_rent / 3

needed_price = hall_rent + price_cake + price_drink + price_animator

print(needed_price)
