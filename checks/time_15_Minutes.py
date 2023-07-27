hour = int(input())
minutes = int(input())

total_time = (hour * 60) + minutes + 15

hour = total_time // 60
minutes = total_time % 60

if hour > 23:
    hour = 0

print(f"{hour}:{minutes:02}")
