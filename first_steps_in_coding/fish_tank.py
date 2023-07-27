length = int(input())
width = int(input())
height = int(input())
percent = float(input())

aquarium = length * width * height
liters = aquarium / 1000 or aquarium * 0.001
space = percent / 100
needed_liters = liters * (1 - space)

print(needed_liters)
