nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


def flat_generator(lst):
    for i in lst:
        for j in i:
            yield j


flat_list = [item for item in flat_generator(nested_list)]
print(flat_list)
