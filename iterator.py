nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:

    def __init__(self, lst):
        self.lst = lst
        self.cursor = -1

    def __iter__(self):
        self.cursor += 1
        self.nested_cursor = 0
        return self

    def __next__(self):
        if self.nested_cursor == len(self.lst[self.cursor]):
            iter(self)
        if self.cursor == len(self.lst):
            raise StopIteration
        self.nested_cursor += 1
        return self.lst[self.cursor][self.nested_cursor - 1]


flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)
