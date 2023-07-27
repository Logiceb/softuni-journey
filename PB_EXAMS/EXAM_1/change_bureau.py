first_row = int(input())
second_row = float(input())
third_row = float(input())

bitcoin = 1168
yuan = 0.15
dollar = 1.76
euro = 1.95

one_bitcoin = first_row * bitcoin
five_yuan = second_row * yuan
half_dollar = five_yuan * dollar

euro_sum = (one_bitcoin + half_dollar) / euro
commission = (third_row * euro_sum) / 100
result = euro_sum - commission

print(f"{result:.2f}")