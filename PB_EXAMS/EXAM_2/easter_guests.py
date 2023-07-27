import math

number_guests = int(input())
budget = int(input())

number_cosunazite = math.ceil(number_guests / 3)
number_eggs = number_guests * 2

price_cosunazite = number_cosunazite * 4
price_eggs = number_eggs * 0.45

total_sum = price_cosunazite + price_eggs

if total_sum <= budget:
    diff = abs(budget - total_sum)
    print(f"Lyubo bought {number_cosunazite} Easter bread and {number_eggs} eggs.")
    print(f"He has {diff:.2f} lv. left.")

else:
    diff = abs(budget - total_sum)
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {diff:.2f} lv. more.")