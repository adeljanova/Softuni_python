actors_name = input()
points_academy = float(input())
num_of_jury = int(input())
points_from_jury = 0
is_over = False
for i in range(num_of_jury):
    name_of_jury = input()
    start_points_of_jury = float(input())
    points_from_jury += len(name_of_jury) * start_points_of_jury / 2
    total_points = points_academy + points_from_jury
    if total_points > 1250.5:
        is_over = True
        break
if is_over:
    print(f"Congratulations, {actors_name} got a nominee for leading role with {total_points:.1f}!")
else:
    difference = abs(1250.5 - total_points)
    print(f"Sorry, {actors_name} you need {difference:.1f} more!")