season = input()
type_of_group = input()
number_of_students = int(input())
number_of_nights = int(input())

price_for_night = 0
sport = ""

if season == "Winter":
    if type_of_group == "boys":
        sport = "Judo"
        price_for_night = 9.6 * number_of_nights * number_of_students
    elif type_of_group == "girls":
        sport = "Gymnastics"
        price_for_night = 9.6 * number_of_nights * number_of_students
    elif type_of_group == "mixed":
        sport = "Ski"
        price_for_night = 10 * number_of_nights * number_of_students
elif season == "Spring":
    if type_of_group == "boys":
        sport = "Tennis"
        price_for_night = 7.2 * number_of_nights * number_of_students
    elif type_of_group == "girls":
        sport = "Athletics"
        price_for_night = 7.2 * number_of_nights * number_of_students
    elif type_of_group == "mixed":
        sport = "Cycling"
        price_for_night = 9.5 * number_of_nights * number_of_students
elif season == "Summer":
    if type_of_group == "boys":
        sport = "Football"
        price_for_night = 15 * number_of_nights * number_of_students
    elif type_of_group == "girls":
        sport = "Volleyball"
        price_for_night = 15 * number_of_nights * number_of_students
    elif type_of_group == "mixed":
        sport = "Swimming"
        price_for_night = 20 * number_of_nights * number_of_students

total_sum = 0

if number_of_students >= 50:
    total_sum = price_for_night - price_for_night * 0.5
elif 20 <= number_of_students < 50:
    total_sum = price_for_night - price_for_night * 0.15
elif 10 <= number_of_students < 20:
    total_sum = price_for_night - price_for_night * 0.05
else:
    total_sum = price_for_night

print(f"{sport} {total_sum:.2f} lv.")
