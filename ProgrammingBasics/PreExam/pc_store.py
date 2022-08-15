procesor = float(input())
video_card = float(input())
ram_memory = float(input())
num_ram = int(input())
discount = float(input())
procesor_in_leva = procesor * 1.57
video_card_in_leva = video_card * 1.57
ram_memory_in_leva = ram_memory * 1.57
total_price_ram = num_ram * ram_memory_in_leva
procesor_in_leva -= procesor_in_leva * discount
video_card_in_leva -= video_card_in_leva * discount
total_price = procesor_in_leva + video_card_in_leva + total_price_ram
print(f"Money needed - {total_price:.2f} leva.")