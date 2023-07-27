import math

series_name = str(input())
number_of_seasons = int(input())
number_of_episodes = int(input())
duration_of_a_regular_episode_without_commercials = float(input())

ad_duration__for_one_episode = duration_of_a_regular_episode_without_commercials * (20 / 100)
length_of_episode_with_ads = duration_of_a_regular_episode_without_commercials + ad_duration__for_one_episode
extra_time_from_the_specials_episodes = number_of_seasons * 10

total_time_to_watch_the_series = math.ceil(length_of_episode_with_ads * number_of_episodes * number_of_seasons + extra_time_from_the_specials_episodes)

print(f"Total time needed to watch the {series_name} series is {total_time_to_watch_the_series} minutes.")