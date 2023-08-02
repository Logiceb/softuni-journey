city = input()
sells = float(input())

com = 0
wrong_error = False

if city == "Sofia":
    if 0 <= sells <= 500:
        com = sells * 0.05
    elif 500 < sells <= 1000:
        com = sells * 0.07
    elif 1000 < sells <= 10000:
        com = sells * 0.08
    elif sells > 10000:
        com = sells * 0.12
    else:
        wrong_error = True

elif city == "Varna":
    if 0 <= sells <= 500:
        com = sells * 0.045
    elif 500 < sells <= 1000:
        com = sells * 0.075
    elif 1000 < sells <= 10000:
        com = sells * 0.1
    elif sells > 10000:
        com = sells * 0.13
    else:
        wrong_error = True

elif city == "Plovdiv":
    if 0 <= sells <= 500:
        com = sells * 0.055
    elif 500 < sells <= 1000:
        com = sells * 0.08
    elif 1000 < sells <= 10000:
        com = sells * 0.12
    elif sells > 10000:
        com = sells * 0.145
    else:
        wrong_error = True

else:
    wrong_error = True

if wrong_error:
    print("error")
else:
    print(f"{com:.2f}")