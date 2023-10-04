import math

number_of_magnolias = int(input())
number_of_hyacinths = int(input())
number_of_roses = int(input())
number_of_cactus = int(input())
price_for_gift = float(input())

total_flower_sum = (number_of_magnolias * 3.25) + (number_of_hyacinths * 4) + (number_of_roses * 3.5) + \
                   (number_of_cactus * 8)

taxes = total_flower_sum * 0.05
profit = total_flower_sum - taxes

price_needed = abs(price_for_gift - profit)

if profit < price_needed:
    print(f"She will have to borrow {math.ceil(price_needed)} leva.")

else:
    print(f"She is left with {math.floor(price_needed)} leva.")

