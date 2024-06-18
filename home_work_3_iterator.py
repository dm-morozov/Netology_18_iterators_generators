class FlatIterator:

    def __init__(self, list_of_list):
        self.item = [iter(list_of_list)]

    def __iter__(self):
        return self

    def __next__(self):
        while self.item:
            try:
                current = next(self.item[-1])
                # print(current)
                if isinstance(current, list):
                    self.item.append(iter(current))
                else:
                    return current
            except StopIteration:
                self.item.pop()
        raise StopIteration


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        # print(flat_iterator_item)
        # print(check_item)
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()