length_in_cm = int(input())
width_in_cm = int(input())
height_in_cm = int(input())
percentage = float(input())

volume_of_the_aquarium = length_in_cm * width_in_cm * height_in_cm
volume_in_liters = volume_of_the_aquarium / 1000
occupied_space = percentage / 100

liters_needed = volume_in_liters * (1 - occupied_space)

print(liters_needed)