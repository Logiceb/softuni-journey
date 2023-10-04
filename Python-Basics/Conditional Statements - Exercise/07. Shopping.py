budget = float(input())
number_gpu = int(input())
number_cpu = int(input())
number_ram = int(input())

gpu = number_gpu * 250
cpu = (gpu * (35 / 100)) * number_cpu
ram = (gpu * (10 / 100)) * number_ram

total_price = gpu + cpu + ram

if number_gpu > number_cpu:
    total_price = total_price - (total_price * (15 / 100))

diff = abs(total_price - budget)

if budget >= total_price:
    print(f"You have {diff:.2f} leva left!")

else:
    print(f"Not enough money! You need {diff:.2f} leva more!")
