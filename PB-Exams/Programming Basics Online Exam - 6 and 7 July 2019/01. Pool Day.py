import math

number_people = int(input())
tax_entrance = float(input())
price_one_lounger = float(input())
price_one_umbrella = float(input())

total_tax_entrance = number_people * tax_entrance
needed_lounger = math.ceil(number_people * (75 / 100))
total_price_lounger = needed_lounger * price_one_lounger
needed_umbrella = math.ceil(number_people / 2)
total_price_umbrella = needed_umbrella * price_one_umbrella

total_price = total_tax_entrance + total_price_lounger + total_price_umbrella

print(f'{total_price:.2f} lv.')