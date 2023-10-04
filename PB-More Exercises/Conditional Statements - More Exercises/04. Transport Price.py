number_of_kilometers = int(input())
day_or_night_travel = input()

transport = 0
tariff = 0

if number_of_kilometers < 20:
    start_up_tax = 0.7
    if day_or_night_travel == "day":
        tariff = 0.79
        transport = tariff * number_of_kilometers + start_up_tax

    elif day_or_night_travel == "night":
        tariff = 0.9
        transport = tariff * number_of_kilometers + start_up_tax

elif 20 <= number_of_kilometers < 100:
    tariff = 0.09
    transport = tariff * number_of_kilometers

else:
    tariff = 0.06
    transport = tariff * number_of_kilometers

print(f"{transport:.2f}")