width = float(input())
height = float(input())

chair_width = 120
width_height = 70

total_width = width * 100
total_height = height * 100

free_row_height = total_height - 100
chair_row_height = free_row_height // width_height
chair_row_width = total_width // chair_width

total = int((chair_row_height * chair_row_width) - 3)
print(total)