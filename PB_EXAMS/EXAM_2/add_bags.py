cost_luggage_20 = float(input())
kg_luggage = float(input())
days_trip = int(input())
number_luggage = int(input())

luggage_tax = 0
price = 0

if kg_luggage < 10:
    luggage_tax = cost_luggage_20 * 0.2

elif 10 < kg_luggage <= 20:
    luggage_tax = cost_luggage_20 * 0.5

elif kg_luggage > 20:
    luggage_tax = cost_luggage_20

price_trip = 0

if days_trip > 30:
    price_trip = luggage_tax + (luggage_tax * 0.1)

elif 7 <= days_trip <= 30:
    price_trip = luggage_tax + (luggage_tax * 0.15)

elif days_trip < 7:
    price_trip = luggage_tax + (luggage_tax * 0.4)

price = price_trip * number_luggage
print(f" The total price of bags is: {price:.2f} lv. ")