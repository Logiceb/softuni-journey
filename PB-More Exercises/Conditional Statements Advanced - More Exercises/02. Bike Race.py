number_of_junior_cyclists = int(input())
number_of_seniors_cyclists = int(input())
track_type = input()

price = 0

if track_type == "trail":
    juniors = 5.5
    seniors = 7
    price = (number_of_junior_cyclists * juniors) + (number_of_seniors_cyclists * seniors)

elif track_type == "cross-country":
    juniors = 8
    seniors = 9.5
    total_cyclists = number_of_junior_cyclists + number_of_seniors_cyclists
    if total_cyclists >= 50:
        discount = (number_of_junior_cyclists * juniors) + (number_of_seniors_cyclists * seniors)
        price = discount - discount * 0.25
    else:
        price = (number_of_junior_cyclists * juniors) + (number_of_seniors_cyclists * seniors)

elif track_type == "downhill":
    juniors = 12.25
    seniors = 13.75
    price = (number_of_junior_cyclists * juniors) + (number_of_seniors_cyclists * seniors)

elif track_type == "road":
    juniors = 20
    seniors = 21.5
    price = (number_of_junior_cyclists * juniors) + (number_of_seniors_cyclists * seniors)

outlay = price * 0.05
remain = price - outlay

print(f"{remain:.2f}")
