budget = float(input())
number_nights = int(input())
price_nights = float(input())
percentage_additional_costs = int(input())

if number_nights > 7:
    price_nights = price_nights * 0.95

total_night = number_nights * price_nights
additional_costs = budget * (percentage_additional_costs / 100)

total_sum = total_night + additional_costs
if total_sum <= budget:
    diff = budget - total_sum
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")

else:
    diff = abs(budget - total_sum)
    print(f"{diff:.2f} leva needed.")