class Node(object):
    current_node = None

    def __init__(self, value, next_=None):
        self._value = value
        self._next = next_

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, n):
        self._next = n

    def __iter__(self):
        self.current_node = self
        return self

    def __next__(self):
        res = self.current_node
        if res is None:
            raise StopIteration
        else:
            self.current_node = self.current_node.next
            return res


def flatten_linked_list(n):
    res = []
    for i in n:
        if isinstance(i.value, Node):
            res = res + flatten_linked_list(i.value)
        else:
            res.append(i.value)
    return res


r1 = Node(1)  # 1 -> None - just one node
r2 = Node(7, Node(2, Node(9)))  # 7 -> 2 -> 9 -> None
# 3 -> (19 -> 25 -> None ) -> 12 -> None
r3 = Node(3, Node(Node(19, Node(25)), Node(12)))
r3_flattenned = flatten_linked_list(r3)  # 3 -> 19 -> 25 -> 12 -> None
r3_expected_flattenned_collection = [3, 19, 25, 12]
assert r3_expected_flattenned_collection == list(r3_flattenned)
