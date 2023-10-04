amount_deposited = float(input())
term_deposit = int(input())
annual_interest_rate = float(input())

calculate_accrued_interest = amount_deposited * (annual_interest_rate / 100)
calculate_interest_one_month = calculate_accrued_interest / 12
total_sum = amount_deposited + term_deposit * calculate_interest_one_month

print(total_sum)
