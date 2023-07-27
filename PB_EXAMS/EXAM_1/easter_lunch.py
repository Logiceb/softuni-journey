number_cozunaci = int(input())
number_eggshells = int(input())
kilograms_cookies = int(input())

cozunaci = 3.20
eggs = 4.35
cookies = 5.40
eggs_dye = 0.15

price_cozunaci = number_cozunaci * cozunaci
price_eggs = number_eggshells * eggs
price_cookies = kilograms_cookies * cookies
price_egg_dye = number_eggshells * 12 * eggs_dye

total_price = price_cozunaci + price_eggs + price_cookies + price_egg_dye

print(f"{total_price:.2f}")