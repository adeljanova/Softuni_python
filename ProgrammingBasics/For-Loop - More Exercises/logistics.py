num_goods = int(input())
microbus = 0
truck = 0
train = 0
microbus_ton = 0
truck_ton = 0
train_ton = 0
for each_goods in range(num_goods):
    goods = int(input())
    if goods <= 3:
        microbus_ton += goods
        microbus += (200 * goods)
    elif goods <= 11:
        truck_ton += goods
        truck += (175 * goods)
    else:
        train_ton += goods
        train += (120 * goods)
total_price = microbus + truck + train
total_ton = microbus_ton + truck_ton + train_ton
average = total_price / total_ton
percent_microbus = microbus_ton / total_ton * 100
percent_truck = truck_ton / total_ton * 100
percent_train = train_ton / total_ton * 100
print(f"{average:.2f}")
print(f"{percent_microbus:.2f}%")
print(f"{percent_truck:.2f}%")
print(f"{percent_train:.2f}%")