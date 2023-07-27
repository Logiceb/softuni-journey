deposit = float(input())
srok_na_deposit = int(input())
godishen_lihven_procent = float(input())

natrupana_lihva = deposit * godishen_lihven_procent / 100
lihva_za_mesec = natrupana_lihva / 12
obshta_suma = deposit + srok_na_deposit * lihva_za_mesec

print(obshta_suma)