movie_name = str(input())
number_of_days = int(input())
number_of_tickets = int(input())
ticket_price = float(input())
percentage_for_the_cinema = int(input())

price_of_tickets_per_day = number_of_tickets * ticket_price
whole_period = number_of_days * price_of_tickets_per_day
percentage_of_the_revenue_remains =  whole_period * percentage_for_the_cinema / 100

income_from_the_film = whole_period - percentage_of_the_revenue_remains

print(f"The profit from the movie {movie_name} is {income_from_the_film:.2f} lv.")