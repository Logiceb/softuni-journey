import math

record_seconds = float(input())
radius_meters = float(input())
time_seconds = float(input())

george_climp = radius_meters * time_seconds
five_meter_time = math.floor(radius_meters / 50) * 30
total_time = george_climp + five_meter_time

diff = abs(total_time - record_seconds)
if record_seconds < total_time:
    print(f"No! He was {diff:.2f} seconds slower.")

elif total_time < record_seconds:
    print(f"Yes! The new record is {total_time:.2f} seconds.")

else:
    print(f"No! He was {diff:.2f} seconds slower.")