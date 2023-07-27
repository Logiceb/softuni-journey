import math

price_of_one_tennis_racket = float(input())
number_of_tennis_rackets = int(input())
number_of_pairs_of_sneakers = int(input())

price_rockets = number_of_tennis_rackets * price_of_one_tennis_racket
price_pair_sneakers = price_of_one_tennis_racket / 6
price_all_sneakers = number_of_pairs_of_sneakers * price_pair_sneakers
price_other_equipment = (price_rockets + price_all_sneakers) * 0.2

total_price = price_rockets + price_all_sneakers + price_other_equipment

price_djokovic = math.floor(total_price / 8)
price_sponsors = math.ceil(total_price * 7 / 8)

print(f"Price to be paid by Djokovic {price_djokovic}")
print(f"Price to be paid by sponsors {price_sponsors}")