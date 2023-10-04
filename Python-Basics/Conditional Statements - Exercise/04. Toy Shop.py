price_of_excursion = float(input())
number_of_puzzle = int(input())
number_of_talking_dolls = int(input())
number_of_teddy_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

# ⦁	Пъзел - 2.60 лв.
# ⦁	Говореща кукла - 3 лв.
# ⦁	Плюшено мече - 4.10 лв.
# ⦁	Миньон - 8.20 лв.
# ⦁	Камионче - 2 лв.

total_price = number_of_puzzle * 2.6 + number_of_talking_dolls * 3 + number_of_teddy_bears * 4.1 + \
              number_of_minions * 8.2 + number_of_trucks * 2

number_toys = number_of_puzzle + number_of_talking_dolls + number_of_teddy_bears + number_of_minions + \
              number_of_trucks

discount = 0

if number_toys >= 50:
    discount = total_price * (25 / 100)

total_sum = total_price - discount
rent = total_sum * (10 / 100)
profit = total_sum - rent

diff = abs(profit - price_of_excursion)

if profit >= price_of_excursion:
    print(f'Yes! {diff:.2f} lv left.')

else:
    print(f'Not enough money! {diff:.2f} lv needed.')