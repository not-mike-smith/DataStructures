from unittest import TestCase
from MaxHeap import MaxHeap


class TestMaxHeap(TestCase):
    def test_MaxHeap(self):
        l = [5, 3, 4, 2, 6, 1]
        h = MaxHeap()
        for item in l:
            h.push(item)
        last_element = 10
        while h.peak() is not None:
            if h.peak() > last_element:
                return self.fail('1 MinHeap return {} last time and {} this time'.format(last_element, h.peak()))
            last_element = h.pop()
        h = MaxHeap(l)
        last_element = 10
        while h.peak() is not None:
            if h.peak() > last_element:
                return self.fail('2 MinHeap return {} last time and {} this time'.format(last_element, h.peak()))
            last_element = h.pop()
        h = MaxHeap(l)
        h.pop()
        h.pop()
        h.push(0)
        h.push(7)
        if h.pop() != 7:
            return self.fail('MaxHeap did not re-heapify')