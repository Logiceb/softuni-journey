name_of_actor = input()
academy_points = float(input())
number_of_assessors = int(input())

total_points = academy_points

for _ in range(number_of_assessors):
    name_of_assessors = input()
    points_of_assessors = float(input())
    total_points += ((len(name_of_assessors) * points_of_assessors) / 2)

    if total_points > 1250.5:
        print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!")
        break

else:
    diff = abs(1250.5 - total_points)
    print(f"Sorry, {name_of_actor} you need {diff:.1f} more!")
