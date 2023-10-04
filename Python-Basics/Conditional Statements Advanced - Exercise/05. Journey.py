budget = float(input())
season = input()

price = 0
location = ""
sleep = ""

if budget <= 100:
    location = "Bulgaria"
    if season == "summer":
        sleep = "Camp"
        price = budget * 0.30
    elif season == "winter":
        sleep = "Hotel"
        price = budget * 0.70

elif budget <= 1000:
    location = "Balkans"
    if season == "summer":
        sleep = "Camp"
        price = budget * 0.40
    elif season == "winter":
        sleep = "Hotel"
        price = budget * 0.80

elif budget > 1000:
    location = "Europe"
    if season == "summer":
        sleep = "Hotel"
        price = budget * 0.90
    elif season == "winter":
        sleep = "Hotel"
        price = budget * 0.90

print(f"Somewhere in {location}")
print(f"{sleep} - {price:.2f}")