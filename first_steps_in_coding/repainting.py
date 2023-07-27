amount_of_nylon = int(input())
amount_of_paint = int(input())
amount_of_razr = int(input())
workers_hours = int(input())

# · Предпазен найлон - 1.50 лв. за кв. метър
# · Боя - 14.50 лв. за литър
# · Разредител за боя - 5.00 лв. за литър

nylon = (amount_of_nylon + 2) * 1.5
paint_percent = (10/100) * amount_of_paint
paint = (amount_of_paint + paint_percent) * 14.5
razr = amount_of_razr * 5

sum_for_materials = nylon + paint + razr + 0.40
workers_sum = (sum_for_materials * 0.30) * workers_hours
total_sum = sum_for_materials + workers_sum

print(total_sum)