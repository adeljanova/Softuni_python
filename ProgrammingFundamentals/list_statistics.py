n = int(input())
main_list = [int(input()) for i in range(n)]
positive_list = []
negative_list = []
count_positive = 0
sum_negative = 0
for number in range(len(main_list)):
    if main_list[number] >= 0:
        positive_list.append(main_list[number])
        count_positive += 1
    else:
        negative_list.append(main_list[number])
        sum_negative += main_list[number]
print(positive_list)
print(negative_list)
print(f"Count of positives: {count_positive}")
print(f"Sum of negatives: {sum_negative}")