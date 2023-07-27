number_guests = int(input())
price_envelope = float(input())
budget_desi = float(input())

if 10 <= number_guests <= 15:
    price_envelope = price_envelope - (price_envelope * 0.15)

elif 15 < number_guests <= 20:
    price_envelope = price_envelope - (price_envelope * 0.2)

elif number_guests > 20:
    price_envelope = price_envelope - (price_envelope * 0.25)

price_cake = (10 * budget_desi) / 100
total_sum = number_guests * price_envelope + price_cake

if total_sum > budget_desi:
    diff = abs(total_sum - budget_desi)
    print(f"No party! {diff:.2f} leva needed.")

elif total_sum < budget_desi:
    diff = abs(budget_desi - total_sum)
    print(f"It is party time! {diff:.2f} leva left.")
