def read_next(*args, **kwargs):
    for arg in args:
        for el in arg:
            yield el

    for kwarg in kwargs.keys():
        for el in kwarg:
            yield el


for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')
