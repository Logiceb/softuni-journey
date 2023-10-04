number_chicken_menu = int(input())
number_fish_menu = int(input())
number_vegetable_menu = int(input())

# • Пилешко меню – 10.35 лв.
# • Меню с риба – 12.40 лв.
# • Вегетарианско меню – 8.15 лв.

price_chicken_menu = number_chicken_menu * 10.35
price_fish_menu = number_fish_menu * 12.40
price_vegetable_menu = number_vegetable_menu * 8.15

total_price_menus = price_chicken_menu + price_fish_menu + price_vegetable_menu
price_dessert = (20 * total_price_menus) / 100
price_delivery = 2.50

total_price_order = total_price_menus + price_dessert + price_delivery

print(total_price_order)
