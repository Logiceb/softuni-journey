month = input()
number_nights = int(input())

studio = 0
apartment = 0

if month == "May" or month == "October":
    studio = number_nights * 50
    apartment = number_nights * 65
    if 7 < number_nights <= 14 and studio:
        studio = studio - (studio * 0.05)
    elif number_nights > 14 and studio:
        studio = studio - (studio * 0.3)
        apartment = apartment - (apartment * 0.1)

elif month == "June" or month == "September":
    studio = number_nights * 75.2
    apartment = number_nights * 68.7
    if number_nights > 14:
        studio = studio - (studio * 0.2)
        apartment = apartment - (apartment * 0.1)

elif month == "July" or month == "August":
    studio = number_nights * 76
    apartment = number_nights * 77
    if number_nights > 14:
        apartment = apartment - (apartment * 0.1)

print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")