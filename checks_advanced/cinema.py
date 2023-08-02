projection_type = input()
rows = int(input())
columns = int(input())

seats = rows * columns
price = 0

if projection_type == "Premiere":
    price = seats * 12

elif projection_type == "Normal":
    price = seats * 7.5

elif projection_type == "Discount":
    price = seats * 5

print(f"{price:.2f} leva")