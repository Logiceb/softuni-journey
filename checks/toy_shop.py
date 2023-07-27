excursion_price = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_teddy = int(input())
number_minions = int(input())
number_trucks = int(input())

total_sum = (number_puzzles * 2.60) + (number_dolls * 3) + (number_teddy * 4.10) + (number_minions * 8.20) + (number_trucks * 2)

number_toys = number_puzzles + number_dolls + number_teddy + number_minions + number_trucks

if number_toys >= 50:
    total_sum = total_sum - (total_sum * 0.25)

total_sum = total_sum - (total_sum * 0.1)

diff = abs(total_sum - excursion_price)

if total_sum >= excursion_price:
    print(f"Yes! {diff:.2f} lv left.")

else:
    print(f"Not enough money! {diff:.2f} lv needed.")