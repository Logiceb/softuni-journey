day_of_week = input()

price_for_ticket = 0

if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Friday":
    price_for_ticket = 12

elif day_of_week == "Wednesday" or day_of_week == "Thursday":
    price_for_ticket = 14

elif day_of_week == "Saturday" or day_of_week == "Sunday":
    price_for_ticket = 16

print(price_for_ticket)