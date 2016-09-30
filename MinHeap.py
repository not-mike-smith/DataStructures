from Heap import OrderedHeap


class MinHeap(OrderedHeap):
    def __init__(self, array=None):
        super(MinHeap, self).__init__(array)

    def _heapier(self, hi, hj):
        if self._list[self._list_index(hi)] <= self._list[self._list_index(hj)]:
            return hi
        else:
            return hj
