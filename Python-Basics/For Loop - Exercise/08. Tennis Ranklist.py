import math

number_of_tournaments_in_which_he_participated = int(input())
starting_number_of_points_in_leaderboard = int(input())

total_points = starting_number_of_points_in_leaderboard
average_points = 0
number_of_wins = 0

for tournaments in range(number_of_tournaments_in_which_he_participated):
    reached_tournament_stage = input()

    if reached_tournament_stage == "W":
        number_of_wins += 1
        total_points += 2000
        average_points += 2000
    elif reached_tournament_stage == "F":
        total_points += 1200
        average_points += 1200
    elif reached_tournament_stage == "SF":
        total_points += 720
        average_points += 720

total_average_points = average_points / number_of_tournaments_in_which_he_participated
percent_winnable_tournaments = (number_of_wins / number_of_tournaments_in_which_he_participated) * 100

print(f"Final points: {math.floor(total_points)}")
print(f"Average points: {math.floor(total_average_points)}")
print(f"{percent_winnable_tournaments:.2f}%")