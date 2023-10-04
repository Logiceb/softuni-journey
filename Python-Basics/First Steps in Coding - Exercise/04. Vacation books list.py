number_pages = int(input())
pages_hour = int(input())
number_days = int(input())

total_time_reading_book = number_pages // pages_hour
needed_hours_day = total_time_reading_book // number_days

print(needed_hours_day)