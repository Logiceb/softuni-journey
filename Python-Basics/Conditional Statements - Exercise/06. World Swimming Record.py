import math

record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds = float(input())

needed_distance = distance_in_meters * time_in_seconds
more_time = math.floor(distance_in_meters / 15) * 12.5
total_time = needed_distance + more_time

diff = abs(record_in_seconds - total_time)

if record_in_seconds <= total_time:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")

else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")