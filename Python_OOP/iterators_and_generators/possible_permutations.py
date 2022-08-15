from itertools import permutations


def possible_permutations(params):

    for perm in permutations(params):
        yield list(perm)


[print(n) for n in possible_permutations([1, 2, 3])]