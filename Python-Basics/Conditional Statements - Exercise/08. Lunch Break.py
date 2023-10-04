import math

serial_name = input()
duration_episode = int(input())
duration_break = int(input())

time_lunch = duration_break / 8
time_relax = duration_break / 4

total_time = duration_break - time_lunch - time_relax

diff = abs(duration_episode - total_time)
rounded_diff = math.ceil(diff)

if total_time >= duration_episode:
    print(f"You have enough time to watch {serial_name} and left with {rounded_diff} minutes free time.")

else:
    print(f"You don't have enough time to watch {serial_name}, you need {rounded_diff} more minutes.")