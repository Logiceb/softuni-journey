first_number = int(input())
second_number = int(input())
operator = input()

result = 0
even_odd = ""
zero_check = False

if operator == "+":
    result = first_number + second_number

elif operator == "-":
    result = first_number - second_number

elif operator == "*":
    result = first_number * second_number

elif operator == "/":
    if second_number == 0:
        zero_check = True
    else:
        result = first_number / second_number

elif operator == "%":
    if second_number == 0:
        zero_check = True
    else:
        result = first_number % second_number

if operator == "+" or operator == "-" or operator == "*":
    if result % 2 == 0:
        even_odd = "even"
        print(f"{first_number} {operator} {second_number} = {result} - {even_odd}")
    else:
        even_odd = "odd"
        print(f"{first_number} {operator} {second_number} = {result} - {even_odd}")

elif operator == "/":
    if zero_check:
        print(f"Cannot divide {second_number} by zero")
    else:
        print(f"{first_number} {operator} {second_number} = {result:.2f}")

elif operator == "%":
    if zero_check:
        print(f"Cannot divide {second_number} by zero")
    else:
        print(f"{first_number} {operator} {second_number} = {result}")