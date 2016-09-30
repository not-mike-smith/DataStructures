from unittest import TestCase
from Heap import Heap


class TestHeap(TestCase):
    @staticmethod
    def token_value():
        return 'a unique value'

    def test__has_child(self):
        h = Heap()
        h.push(0)
        h.push(1)
        h.push(2)
        if not h._has_child(h._heap_index(0)):
            return self.fail('Heap with 3 items, 1st item has a child')
        if h._has_child(h._heap_index(1)):
            return self.fail('Heap with 3 items, 2nd item has no child')

    def test__has_right_child(self):
        h = Heap()
        h.push(0)
        h.push(1)
        if not h._has_child(h._heap_index(0)):
            return self.fail('Heap with 2 items, 1st item has a child')
        if h._has_child(h._heap_index(1)):
            return self.fail('Heap with 2 items, 2nd item has no child')

    def test__swap(self):
        h = Heap()
        h.push(0)
        h.push(1)
        h._swap(1, 2)
        if h.pop() != 1:
            return self.fail('swap did not swap 2 element heap')
        if h.pop() != 0:
            return self.fail('swap did not swap 2 element heap')
        h.push(1)
        h.push(2)
        h.push(3)
        h.push(4)
        h.push(5)
        h._swap(1, 5)
        if h.pop() != 5:
            return self.fail('swap did not swap element 1 and 5')
        if h.pop() != 2:
            return self.fail('swap messed up the pieces between the swapped elements')
        if h.pop() != 3:
            return self.fail('swap messed up the pieces between the swapped elements')
        if h.pop() != 4:
            return self.fail('swap messed up the pieces between the swapped elements')
        if h.pop() != 1:
            return self.fail('swap did not swap element 5 and 1')

    def test_push(self):
        h = Heap()
        h.push(self.token_value())
        if not len(h) == 1:
            return self.fail('push did not increment length')
        if h._list[0] != self.token_value():
            return self.fail('push did not add the right value')

    def test_pop(self):
        h = Heap()
        h.push(self.token_value())
        temp = h.pop()
        if len(h) != 0:
            return self.fail('pop did not decrement length')
        if temp != self.token_value():
            return self.fail('pop did not return the correct value')
