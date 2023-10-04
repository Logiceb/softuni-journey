import math

number_of_days = int(input())
food_left_in_kilograms = int(input())
food_per_day_for_dog_in_kilograms = float(input())
food_per_day_for_cat_in_kilograms = float(input())
food_per_day_for_turtle_in_kilograms = float(input())

necessary_food_for_dog = number_of_days * food_per_day_for_dog_in_kilograms
necessary_food_for_cat = number_of_days * food_per_day_for_cat_in_kilograms
necessary_food_for_turtle = (number_of_days * food_per_day_for_turtle_in_kilograms) / 1000

total_food = necessary_food_for_dog + necessary_food_for_cat + necessary_food_for_turtle

food_diff = abs(food_left_in_kilograms - total_food)

if total_food <= food_left_in_kilograms:
    print(f"{math.floor(food_diff)} kilos of food left.")

else:
    print(f"{math.ceil(food_diff)} more kilos of food are needed.")