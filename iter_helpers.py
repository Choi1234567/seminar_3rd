import itertools
from _operator import mul

# document for itertools:  https://docs.python.org/3/library/itertools.html#itertools.groupby


def transpose(it):
    return itertools.zip_longest(it[0], it[1])


def scalar_product(a, b):
    try:
        a1 = map(float, a)
        a2 = map(float, b)
        return sum(itertools.starmap(mul, itertools.zip_longest(a1, a2)))
        print(res)
    except ValueError:
        return None


expected = [[1, 2], [-1, 3]]
actual = transpose([[1, -1], [2, 3]])
assert expected == list(map(list, actual))

expected = 1
actual = scalar_product([1, '2'], [-1, 1])
assert expected == actual
actual = scalar_product([1, 'xyz'], [-1, 1])
assert actual is None
