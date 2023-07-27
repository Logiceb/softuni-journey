import math

record_sec = float(input())
distance_meters = float(input())
time_second = float(input())

swim = distance_meters * time_second
delay = math.floor(distance_meters / 15) * 12.5

total_time = swim + delay

if record_sec <= total_time:
    diff = total_time - record_sec
    print(f"No, he failed! He was {diff:.2f} seconds slower.")

else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")