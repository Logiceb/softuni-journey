minutes_walk = int(input())
number_walk = int(input())
cat_calories = int(input())

cat_walk_day = minutes_walk * number_walk
total_burn_calories = cat_walk_day * 5
five_calories_day = cat_calories * 0.5

if total_burn_calories >= five_calories_day:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_burn_calories}.")

else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_burn_calories}.")