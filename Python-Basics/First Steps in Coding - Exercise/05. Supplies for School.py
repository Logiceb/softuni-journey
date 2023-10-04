number_packets_chemicals = int(input())
number_packets_tag = int(input())
liters_chalkboard_cleaner = int(input())
percentage_reduction = int(input())

# • Пакет химикали - 5.80 лв.
# • Пакет маркери - 7.20 лв.
# # • Препарат - 1.20 лв (за литър)

price_chemical_packages = number_packets_chemicals * 5.80
price_tag_packages = number_packets_tag * 7.20
price_preparation = liters_chalkboard_cleaner * 1.20
price_all_materials = price_chemical_packages + price_tag_packages + price_preparation

price_with_discount = price_all_materials - (price_all_materials * (percentage_reduction / 100))

print(price_with_discount)