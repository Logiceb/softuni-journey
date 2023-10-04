season = input()
km_months = float(input())

salary = 0

if km_months <= 5000:
    if season == "Spring" or season == "Autumn":
        salary = (km_months * 0.75) * 4
    elif season == "Summer":
        salary = (km_months * 0.90) * 4
    elif season == "Winter":
        salary = (km_months * 1.05) * 4
elif 5000 <= km_months <= 10000:
    if season == "Spring" or season == "Autumn":
        salary = (km_months * 0.95) * 4
    elif season == "Summer":
        salary = (km_months * 1.1) * 4
    elif season == "Winter":
        salary = (km_months * 1.25) * 4
elif 10000 < km_months <= 20000:
    salary = (km_months * 1.45) * 4

total_salary = salary - salary * 0.1

print(f"{total_salary:.2f}")