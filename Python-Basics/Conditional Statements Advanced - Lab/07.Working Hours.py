hour_night = int(input())
day_week = input()

if day_week == "Monday" or day_week == "Tuesday" or day_week == "Wednesday" or day_week == "Thursday" or\
        day_week == "Friday" or day_week == "Saturday":
    if 10 <= hour_night <= 18:
        print("open")
    else:
        print("closed")
else:
    print("closed")