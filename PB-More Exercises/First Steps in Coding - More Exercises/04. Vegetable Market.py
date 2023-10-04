first_row = float(input())
second_row = float(input())
third_row = int(input())
fourth_row = int(input())

vegetables_cost = first_row * third_row
fruits_cost = second_row * fourth_row

total_price = vegetables_cost + fruits_cost
euro = total_price / 1.94

print(f'{euro:.2f}')