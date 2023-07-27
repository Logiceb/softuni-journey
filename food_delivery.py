chicken_menu = int(input())
fish_menu = int(input())
veg_menu = int(input())

# • Пилешко меню – 10.35 лв.
# • Меню с риба – 12.40 лв.
# • Вегетарианско меню – 8.15 лв.

chicken = chicken_menu * 10.35
fish = fish_menu * 12.40
veg = veg_menu * 8.15

all_menus = chicken + fish + veg
dessert = (20/100) * all_menus
delivery_price = 2.50

total_price = all_menus + dessert + delivery_price

print(total_price)