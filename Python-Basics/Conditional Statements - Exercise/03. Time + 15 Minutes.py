import math

hours = int(input())
minutes = int(input())

hours_to_minutes = hours * 60

total_minutes = hours_to_minutes + minutes + 15

hours = total_minutes / 60
minutes = total_minutes % 60

hours = math.floor(hours)

if hours > 23:
    hours = 0

if minutes < 10:
    print(f"{hours}:0{minutes}")

else:
    print(f"{hours}:{minutes}")

