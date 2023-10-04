number_of_days_off = int(input())

holidays = number_of_days_off * 127
working_days = (365 - number_of_days_off) * 63
total_time = holidays + working_days

diff = abs(30000 - total_time)

hours = diff // 60
minutes = diff % 60

if total_time > 30000:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")

if total_time < 30000:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
