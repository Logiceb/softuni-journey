number_of_groups = int(input())

total_people = 0
climbing_musala = 0
climbing_montblanc = 0
climbing_kilimanjaro = 0
climbing_K2 = 0
climbing_everest = 0

for groups in range(number_of_groups):
    number_of_people = int(input())
    total_people += number_of_people

    if number_of_people <= 5:
        climbing_musala += number_of_people
    elif 6 <= number_of_people <= 12:
        climbing_montblanc += number_of_people
    elif 13 <= number_of_people <= 25:
        climbing_kilimanjaro += number_of_people
    elif 26 <= number_of_people <= 40:
        climbing_K2 += number_of_people
    else:
        climbing_everest += number_of_people

total_climbing_musala = climbing_musala / total_people * 100
total_climbing_montblanc = climbing_montblanc / total_people * 100
total_climbing_kilimanjaro = climbing_kilimanjaro / total_people * 100
total_climbing_K2 = climbing_K2 / total_people * 100
total_climbing_everest = climbing_everest / total_people * 100

print(f"{total_climbing_musala:.2f}%")
print(f"{total_climbing_montblanc:.2f}%")
print(f"{total_climbing_kilimanjaro:.2f}%")
print(f"{total_climbing_K2:.2f}%")
print(f"{total_climbing_everest:.2f}%")
