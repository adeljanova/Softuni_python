card_deck = input().split()
shuffle_times = int(input())
final_deck = []
for time in range(1, shuffle_times + 1):
    final_deck = []
    middle = len(card_deck) // 2
    left_half = card_deck[0:middle]
    right_half = card_deck[middle::]
    for index in range(len(left_half)):
        final_deck.append(left_half[index])
        final_deck.append(right_half[index])
    card_deck = final_deck
print(card_deck)