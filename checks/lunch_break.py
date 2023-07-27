import math

name_serial = input()
episode_length = int(input())
break_length = int(input())

time_lunch = break_length / 8
time_relax = break_length / 4
free_time = break_length - time_lunch - time_relax

diff = abs(free_time - episode_length)
rounded_diff = math.ceil(diff)
if free_time >= episode_length:
    print(f"You have enough time to watch {name_serial} and left with {rounded_diff} minutes free time.")

else:
    print(f"You don't have enough time to watch {name_serial}, you need {rounded_diff} more minutes.")