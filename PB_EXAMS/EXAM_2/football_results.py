fisrt_match = input()
second_match = input()
third_match = input()

win = 0
lost = 0
even = 0

if ord(fisrt_match[0]) > ord(fisrt_match[2]):
    win += 1
elif ord(fisrt_match[0]) < ord(fisrt_match[2]):
    lost += 1
else:
    even += 1

if ord(second_match[0]) > ord(second_match[2]):
    win += 1
elif ord(second_match[0]) < ord(second_match[2]):
    lost += 1
else:
    even += 1

if ord(third_match[0]) > ord(third_match[2]):
    win += 1
elif ord(third_match[0]) < ord(third_match[2]):
    lost += 1
else:
    even += 1

print(f"Team won {win} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {even}")