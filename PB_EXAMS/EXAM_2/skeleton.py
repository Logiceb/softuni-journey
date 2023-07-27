minutes_control = int(input())
seconds_control = int(input())
length_meters = float(input())
seconds_100_meters = int(input())

calculation = minutes_control * 60 + seconds_control
calculation_decrease = length_meters / 120
total_decrease_time = calculation_decrease * 2.5
time_martin = (length_meters / 100) * seconds_100_meters - total_decrease_time

if time_martin <= calculation:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {time_martin:.3f}.")

else:
    diff = abs(time_martin - calculation)
    print(f"No, Marin failed! He was {diff:.3f} second slower.")