team_a = []
team_b = []
for num1 in range(1, 12):
    team_a.append(f"A-{num1}")
for num2 in range(1, 12):
    team_b.append(f"B-{num2}")
sequence_of_cards = input().split()
counter_a = 11
counter_b = 11
was_terminated = False
for card in sequence_of_cards:
    if card in team_a:
        team_a.remove(card)
        counter_a -= 1
    elif card in team_b:
        team_b.remove(card)
        counter_b -= 1
    if counter_a < 7 or counter_b < 7:
        was_terminated = True
        break
print(f"Team A - {counter_a}; Team B - {counter_b}")
if was_terminated:
    print("Game was terminated")
