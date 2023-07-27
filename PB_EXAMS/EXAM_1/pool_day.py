import math

number_of_people = int(input())
tax = float(input())
price_sezlong = float(input())
price_umbrella = float(input())

vhodna_taksa = number_of_people * tax
nujni_sezlongi = math.ceil(number_of_people * 0.75)
nujnI_chaduri = math.ceil(number_of_people / 2.0)
total_price = vhodna_taksa + (nujni_sezlongi * price_sezlong) + (nujnI_chaduri * price_umbrella)

#print(total_price)
print(f"{total_price:.2f} lv.")