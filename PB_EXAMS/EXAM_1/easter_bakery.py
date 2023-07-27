price_flour_kilogram = float(input())
kilograms_flour = float(input())
kilograms_sugar = float(input())
number_eggshells = int(input())
packets_yeast = int(input())

price_sugar = price_flour_kilogram - ((25 / 100) * price_flour_kilogram)
price_eggs = price_flour_kilogram + ((10 / 100) * price_flour_kilogram)
price_yeast = price_sugar - ((80 / 100) * price_sugar)

sum_flour = price_flour_kilogram * kilograms_flour
sum_sugar = price_sugar * kilograms_sugar
sum_eggs = price_eggs * number_eggshells
sum_yeast = price_yeast * packets_yeast

total_price = sum_flour + sum_sugar + sum_eggs + sum_yeast

print(f"{total_price:.2f}")