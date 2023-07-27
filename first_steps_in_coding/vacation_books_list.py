# from math import floor

broi_stranici = int(input())
stranici_za_chas = int(input())
broi_dni = int(input())

obshto_vreme_za_chetene = broi_stranici // stranici_za_chas
neobhodimi_chasove = obshto_vreme_za_chetene // broi_dni

print(neobhodimi_chasove)