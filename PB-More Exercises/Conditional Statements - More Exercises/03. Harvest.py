import math

x_cubic_meters_vineyard = int(input())
y_grapes_for_one_cubic_meters = float(input())
z_required_liters_of_wine = int(input())
number_of_workers = int(input())

total_grapes = x_cubic_meters_vineyard * y_grapes_for_one_cubic_meters
wine = 0.40 * total_grapes / 2.5

diff_wine = abs(wine - z_required_liters_of_wine)
wine_per_person = diff_wine / number_of_workers

if wine >= z_required_liters_of_wine:
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    print(f"{math.ceil(diff_wine)} liters left -> {math.ceil(wine_per_person)} liters per person.")

else:
    print(f"It will be a tough winter! More {math.floor(diff_wine)} liters wine needed.")