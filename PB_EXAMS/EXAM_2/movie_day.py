time_pics = int(input())
number_scenes = int(input())
duration_scene = int(input())

field_preparation = time_pics * 0.15
time_shoot_scenes = number_scenes * duration_scene

all_time = field_preparation + time_shoot_scenes

diff = abs(time_pics - all_time)
rounded_diff = round(diff)
if all_time <= time_pics:
    print(f"You managed to finish the movie on time! You have {rounded_diff} minutes left!")

else:
    print(f"Time is up! To complete the movie you need {rounded_diff} minutes.")