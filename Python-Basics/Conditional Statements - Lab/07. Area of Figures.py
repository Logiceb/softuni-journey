import math

type_of_figure = input()

if type_of_figure == "square":
    side_length = float(input())
    face = side_length * side_length
    print(f"{face:.3f}")

elif type_of_figure == "rectangle":
    length = float(input())
    side = float(input())
    face = length * side
    print(f"{face:.3f}")

elif type_of_figure == "circle":
    radius = float(input())
    face = math.pi * (radius * radius)
    print(f"{face:.3f}")

elif type_of_figure == "triangle":
    side = float(input())
    height = float(input())
    face = side * height / 2
    print(f"{face:.3f}")