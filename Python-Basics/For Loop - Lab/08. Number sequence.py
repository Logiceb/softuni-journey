import sys

n = int(input())

max_sum = -sys.maxsize
min_sum = sys.maxsize

for _ in range(n):
    current_number = int(input())

    if current_number > max_sum:
        max_sum = current_number
    if current_number < min_sum:
        min_sum = current_number

print(f"Max number: {max_sum}")
print(f"Min number: {min_sum}")
