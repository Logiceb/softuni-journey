exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time = (exam_hour * 60) + exam_minute
arrival_time = (arrival_hour * 60) + arrival_minute
diff = abs(exam_time - arrival_time)

if arrival_time > exam_time:
    print("Late")
    if diff >= 60:
        hour = diff // 60
        minutes = diff % 60
        print(f"{hour}:{minutes:02d} hours after the start")
    else:
        print(f"{diff} minutes after the start")

elif arrival_time == exam_time or diff <= 30:
    print("On Time")
    if diff > 0:
        print(f"{diff} minutes before the start")

else:
    print("Early")
    if diff >= 60:
        hour = diff // 60
        minutes = diff % 60
        print(f"{hour}:{minutes:02d} hours before the start")
    else:
        print(f"{diff} minutes before the start")