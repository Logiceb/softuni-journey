number_of_chrysanthemums_purchased = int(input())
number_of_roses_purchased = int(input())
number_of_tulips_purchased = int(input())
season = input()
whether_day_is_a_holiday = input()

price = 0
all_flowers = number_of_roses_purchased + number_of_tulips_purchased + number_of_chrysanthemums_purchased

if season == "Spring" or season == "Summer":
    chrysanthemums_price = number_of_chrysanthemums_purchased * 2
    roses_price = number_of_roses_purchased * 4.1
    tulips_price = number_of_tulips_purchased * 2.5
    price = chrysanthemums_price + roses_price + tulips_price

elif season == "Autumn" or season == "Winter":
    chrysanthemums_price = number_of_chrysanthemums_purchased * 3.75
    roses_price = number_of_roses_purchased * 4.5
    tulips_price = number_of_tulips_purchased * 4.15
    price = chrysanthemums_price + roses_price + tulips_price

if whether_day_is_a_holiday == "Y":
    price = price + price * 0.15

if number_of_tulips_purchased > 7 and season == "Spring":
    price = price - price * 0.05

if number_of_roses_purchased >= 10 and season ==  "Winter":
    price = price - price * 0.10

if all_flowers > 20:
    price = price - price * 0.20

price_to_arrange = price + 2

print(f"{price_to_arrange:.2f}")