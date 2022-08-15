price_for_1kg_skumriq = float(input())
price_for_1kg_caca = float(input())
kg_palamud = float(input())
kg_safrid = float(input())
kg_midi = int(input())
price_palamud = price_for_1kg_skumriq + price_for_1kg_skumriq * 3 / 5
price_safrid = price_for_1kg_caca + price_for_1kg_caca * 4 / 5
price_midi = 7.50
sum_palamud = kg_palamud * price_palamud
sum_safrid = kg_safrid * price_safrid
sum_midi = kg_midi * price_midi
total_sum = sum_midi + sum_safrid + sum_palamud
print(f"{total_sum:.2f}")