set_n_len, set_m_len = map(int, input().split())
set_n = set()
set_m = set()

for _ in range(set_n_len):
    num = int(input())
    set_n.add(num)

for _ in range(set_m_len):
    num = int(input())
    set_m.add(num)

[print(item) for item in set_n.intersection(set_m)]
