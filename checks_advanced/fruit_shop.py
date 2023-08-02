fruit = input()
day_of_week = input()
quantity = float(input())

quantity_price = 0
check_error = False

if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or \
        day_of_week == "Thursday" or day_of_week == "Friday":
    if fruit == "banana":
        quantity_price = quantity * 2.5
    elif fruit == "apple":
        quantity_price = quantity * 1.2
    elif fruit == "orange":
        quantity_price = quantity * 0.85
    elif fruit == "grapefruit":
        quantity_price = quantity * 1.45
    elif fruit == "kiwi":
        quantity_price = quantity * 2.7
    elif fruit == "pineapple":
        quantity_price = quantity * 5.5
    elif fruit == "grapes":
        quantity_price = quantity * 3.85
    else:
        check_error = True

elif day_of_week == "Saturday" or day_of_week == "Sunday":
    if fruit == "banana":
        quantity_price = quantity * 2.7
    elif fruit == "apple":
        quantity_price = quantity * 1.25
    elif fruit == "orange":
        quantity_price = quantity * 0.9
    elif fruit == "grapefruit":
        quantity_price = quantity * 1.60
    elif fruit == "kiwi":
        quantity_price = quantity * 3
    elif fruit == "pineapple":
        quantity_price = quantity * 5.6
    elif fruit == "grapes":
        quantity_price = quantity * 4.2
    else:
        check_error = True

else:
    check_error = True

if check_error:
    print("error")

else:
    print(f"{quantity_price:.2f}")