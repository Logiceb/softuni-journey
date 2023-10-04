text = input()

sum = 0

for word in text:
    if word == "a":
        sum += 1
    if word == "e":
        sum += 2
    if word == "i":
        sum += 3
    if word == "o":
        sum += 4
    if word == "u":
        sum += 5

print(sum)