number_of_pen = int(input())
number_of_marker = int(input())
liters_of_prep = int(input())
percent_discount = int(input())

# • Пакет химикали - 5.80 лв.
# • Пакет маркери - 7.20 лв.
# • Препарат - 1.20 лв (за литър)

pen = number_of_pen * 5.80
marker = number_of_marker * 7.20
prep = liters_of_prep * 1.20
discount = percent_discount / 100

all_materials = pen + marker + prep
price_with_discount = all_materials - (all_materials * discount)

print(price_with_discount)

