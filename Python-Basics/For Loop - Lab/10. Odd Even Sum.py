n = int(input())

odd = 0
even = 0

for i in range(n):
    number = int(input())
    if i % 2 == 0:
        even += number
    else:
        odd += number

if odd == even:
    print("Yes")
    print(f"Sum = {odd}")
else:
    diff = abs(odd - even)
    print("No")
    print(f"Diff = {diff}")
