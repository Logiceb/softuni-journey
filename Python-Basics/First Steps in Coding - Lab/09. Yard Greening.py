meters = float(input())

price_green = meters * 7.61
discount = 0.18 * price_green
total_price = price_green - discount

print(f"The final price is: {total_price} lv.")
print(f"The discount is: {discount} lv.")