def get_primes(params):
    flag = False
    for num in params:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    flag = True
            if flag:
                flag = False
            else:
                yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
