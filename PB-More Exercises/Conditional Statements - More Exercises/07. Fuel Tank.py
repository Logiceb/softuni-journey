type_fuel = input()
fuel_liters = float(input())

if type_fuel == "Diesel":
    if fuel_liters >= 25:
        print(f"You have enough diesel.")

    elif fuel_liters < 25:
        print(f"Fill your tank with diesel!")

elif type_fuel == "Gasoline":
    if fuel_liters >= 25:
        print(f"You have enough gasoline.")

    elif fuel_liters < 25:
        print(f"Fill your tank with gasoline!")

elif type_fuel == "Gas":
    if fuel_liters >= 25:
        print(f"You have enough gas.")

    elif fuel_liters < 25:
        print(f"Fill your tank with gas!")

else:
    print("Invalid fuel!")
