annual_free_for_basketball_practice = int(input())

price_basketball_shoes = annual_free_for_basketball_practice - (annual_free_for_basketball_practice * (40 / 100))
price_basketball_suit = price_basketball_shoes - (price_basketball_shoes * 0.2)
price_basketball_ball = price_basketball_suit / 4
basketball_accessories = price_basketball_ball / 5

total_price_equipment = annual_free_for_basketball_practice + price_basketball_shoes + price_basketball_suit + \
                        price_basketball_ball + basketball_accessories

print(total_price_equipment)
