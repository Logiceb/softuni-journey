type_fuel = input()
amount_of_fuel = float(input())
possession_of_club_card = input()

fuel_price = 0

if type_fuel == "Gas":
    if possession_of_club_card == "Yes":
        discount = 0.93 - 0.08
        if 20 <= amount_of_fuel <= 25:
            fuel_price = (amount_of_fuel * discount) - (amount_of_fuel * discount) * 0.08
        elif amount_of_fuel > 25:
            fuel_price = (amount_of_fuel * discount) - (amount_of_fuel * discount) * 0.10
        else:
            fuel_price = amount_of_fuel * discount

    elif possession_of_club_card == "No":
        if 20 <= amount_of_fuel <= 25:
            fuel_price = (amount_of_fuel * 0.93) - (amount_of_fuel * 0.93) * 0.08
        elif amount_of_fuel > 25:
            fuel_price = (amount_of_fuel * 0.93) - (amount_of_fuel * 0.93) * 0.10
        else:
            fuel_price = amount_of_fuel * 0.93

elif type_fuel == "Gasoline":
    if possession_of_club_card == "Yes":
        discount = 2.22 - 0.18
        if 20 <= amount_of_fuel <= 25:
            fuel_price = (amount_of_fuel * discount) - (amount_of_fuel * discount) * 0.08
        elif amount_of_fuel > 25:
            fuel_price = (amount_of_fuel * discount) - (amount_of_fuel * discount) * 0.10
        else:
            fuel_price = amount_of_fuel * discount

    elif possession_of_club_card == "No":
        if 20 <= amount_of_fuel <= 25:
            fuel_price = (amount_of_fuel * 2.22) - (amount_of_fuel * 2.22) * 0.08
        elif amount_of_fuel > 25:
            fuel_price = (amount_of_fuel * 2.22) - (amount_of_fuel * 2.22) * 0.10
        else:
            fuel_price = amount_of_fuel * 2.22

elif type_fuel == "Diesel":
    if possession_of_club_card == "Yes":
        discount = 2.33 - 0.12
        if 20 <= amount_of_fuel <= 25:
            fuel_price = (amount_of_fuel * discount) - (amount_of_fuel * discount) * 0.08
        elif amount_of_fuel > 25:
            fuel_price = (amount_of_fuel * discount) - (amount_of_fuel * discount) * 0.10
        else:
            fuel_price = amount_of_fuel * discount

    elif possession_of_club_card == "No":
        if 20 <= amount_of_fuel <= 25:
            fuel_price = (amount_of_fuel * 2.33) - (amount_of_fuel * 2.33) * 0.08
        elif amount_of_fuel > 25:
            fuel_price = (amount_of_fuel * 2.33) - (amount_of_fuel * 2.33) * 0.10
        else:
            fuel_price = amount_of_fuel * 2.33

print(f"{fuel_price:.2f} lv.")
