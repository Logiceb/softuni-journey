city = input()
sells = float(input())

sells_sum = 0
check_error = False

if city == "Sofia":
    if 0 <= sells <= 500:
        sells_sum = sells * 0.05
    elif 500 < sells <= 1000:
        sells_sum = sells * 0.07
    elif 1000 < sells <= 10000:
        sells_sum = sells * 0.08
    elif sells > 10000:
        sells_sum = sells * 0.12
    else:
        check_error = True

elif city == "Varna":
    if 0 <= sells <= 500:
        sells_sum = sells * 0.045
    elif 500 < sells <= 1000:
        sells_sum = sells * 0.075
    elif 1000 < sells <= 10000:
        sells_sum = sells * 0.10
    elif sells > 10000:
        sells_sum = sells * 0.13
    else:
        check_error = True

elif city == "Plovdiv":
    if 0 <= sells <= 500:
        sells_sum = sells * 0.055
    elif 500 < sells <= 1000:
        sells_sum = sells * 0.08
    elif 1000 < sells <= 10000:
        sells_sum = sells * 0.12
    elif sells > 10000:
        sells_sum = sells * 0.145
    else:
        check_error = True

else:
    check_error = True

if check_error:
    print("error")

else:
    print(f"{sells_sum:.2f}")