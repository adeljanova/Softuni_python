from collections import deque

bullet_price = int(input())
size_of_the_gun_barrel = int(input())
bullets = deque(map(int, input().split()))
locks = deque(map(int, input().split()))
value_of_the_intelligence = int(input())
num_of_bullets = len(bullets)
bullet_counter = 0
counter = 0

while True:

    if counter == size_of_the_gun_barrel:
        if len(bullets) > 0:
            counter = 0
            print("Reloading!")

    if len(bullets) > 0:
        current_bullet = bullets.pop()
        if len(locks) > 0:
            bullet_counter += 1
    else:
        break

    if len(locks) > 0:
        current_lock = locks.popleft()
    else:
        break

    if current_bullet > current_lock:
        locks.appendleft(current_lock)
        counter += 1
        print("Ping!")
    else:
        counter += 1
        print("Bang!")

if len(locks) == 0:
    print(f"{num_of_bullets - bullet_counter} bullets left. Earned ${value_of_the_intelligence - (bullet_counter * bullet_price)}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")


