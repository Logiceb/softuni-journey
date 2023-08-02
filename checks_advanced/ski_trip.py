days = int(input())
type_room = input()
rating = input()

room_for_one_person = 18
apartment = 25
president_apartment = 35

days_room_for_one_person = (days - 1) * room_for_one_person
days_apartment = (days - 1) * apartment
days_president_apartment = (days - 1) * president_apartment

price = 0

if days < 10:
    if type_room == "room for one person":
        price = days_room_for_one_person
        if rating == "positive":
            price = price + (price * 0.25)
        elif rating == "negative":
            price = price - (price * 0.1)
    elif type_room == "apartment":
        price = days_apartment - (days_apartment * 0.3)
        if rating == "positive":
            price = price + (price * 0.25)
        elif rating == "negative":
            price = price - (price * 0.1)
    elif type_room == "president apartment":
        price = days_president_apartment - (days_president_apartment * 0.1)
        if rating == "positive":
            price = price + (price * 0.25)
        elif rating == "negative":
            price = price - (price * 0.1)

elif 10 < days < 15:
    if type_room == "room for one person":
        price = days_room_for_one_person
        if rating == "positive":
            price = price + (price * 0.25)
        elif rating == "negative":
            price = price - (price * 0.1)
    elif type_room == "apartment":
        price = days_apartment - (days_apartment * 0.35)
        if rating == "positive":
            price = price + (price * 0.25)
        elif rating == "negative":
            price = price - (price * 0.1)
    elif type_room == "president apartment":
        price = days_president_apartment - (days_president_apartment * 0.15)
        if rating == "positive":
            price = price + (price * 0.25)
        elif rating == "negative":
            price = price - (price * 0.1)

elif days > 15:
    if type_room == "room for one person":
        price = days_room_for_one_person
        if rating == "positive":
            price = price + (price * 0.25)
        elif rating == "negative":
            price = price - (price * 0.1)
    elif type_room == "apartment":
        price = days_apartment - (days_apartment * 0.5)
        if rating == "positive":
            price = price + (price * 0.25)
        elif rating == "negative":
            price = price - (price * 0.1)
    elif type_room == "president apartment":
        price = days_president_apartment - (days_president_apartment * 0.2)
        if rating == "positive":
            price = price + (price * 0.25)
        elif rating == "negative":
            price = price - (price * 0.1)

print(f"{price:.2f}")