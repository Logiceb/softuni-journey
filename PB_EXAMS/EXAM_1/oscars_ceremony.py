rent_tax = int(input())

price_for_statuettes = rent_tax - (30 / 100) * rent_tax
catering_price = price_for_statuettes - (15 / 100) * price_for_statuettes
sounding_price = catering_price / 2

total_price = rent_tax + price_for_statuettes + catering_price + sounding_price

print(f"{total_price:.2f}")