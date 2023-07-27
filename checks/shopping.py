budget = float(input())
number_gpu = int(input())
number_cpu = int(input())
number_ram = int(input())

# · Видеокарта – 250 лв./бр.
# · Процесор – 35% от цената на закупените видеокарти/бр.
# · Рам памет – 10% от цената на закупените видеокарти/бр.

gpu = number_gpu * 250
cpu = number_cpu * (gpu * 0.35)
ram = number_ram * (gpu * 0.1)

total_sum = gpu + cpu + ram

if number_gpu > number_cpu:
    total_sum = total_sum - (total_sum * 0.15)

if total_sum <= budget:
    diff = abs(budget - total_sum)
    print(f"You have {diff:.2f} leva left!")

else:
    diff = abs(total_sum - budget)
    print(f"Not enough money! You need {diff:.2f} leva more!")