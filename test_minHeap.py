from unittest import TestCase
from MinHeap import MinHeap


class TestMinHeap(TestCase):
    def test_minHeap(self):
        l = [5, 3, 4, 2, 6, 1]
        h = MinHeap()
        for item in l:
            h.push(item)
        last_element = 0
        while h.peak() is not None:
            if h.peak() < last_element:
                return self.fail('1 MinHeap return {} last time and {} this time'.format(last_element, h.peak()))
            last_element = h.pop()
        h = MinHeap(l)
        last_element = 0
        while h.peak() is not None:
            if h.peak() < last_element:
                return self.fail('2 MinHeap return {} last time and {} this time'.format(last_element, h.peak()))
            last_element = h.pop()
        h = MinHeap(l)
        h.pop()
        h.pop()
        h.push(0)
        h.push(7)
        if h.pop() != 0:
            return self.fail('MinHeap did not re-heapify')
