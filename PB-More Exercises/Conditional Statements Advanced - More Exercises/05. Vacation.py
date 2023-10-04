budget = float(input())
season = input()

accommodation = ""
location = ""
total_sum = 0

if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        total_sum = budget * 0.65
    elif season == "Winter":
        total_sum = budget * 0.45
elif 100 < budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        total_sum = budget * 0.80
    elif season == "Winter":
        total_sum = budget * 0.60
elif budget > 3000:
    accommodation = "Hotel"
    if season == "Summer":
        total_sum = budget * 0.90
    elif season == "Winter":
        total_sum = budget * 0.90

if season == "Summer":
    location = "Alaska"
elif season == "Winter":
    location = "Morocco"

print(f"{location} - {accommodation} - {total_sum:.2f}")