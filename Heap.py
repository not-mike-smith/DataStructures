from abc import ABCMeta, abstractmethod


class Heap(object):
    def __init__(self, array=None):
        """
        :param array: array(list) to make heap from.  One is created if None is passed
        :return: a heap
        """
        if array is not None:
            self._list = list(array)
        else:
            self._list = []

    def __len__(self):
        return len(self._list)

    @staticmethod
    def _heap_index(li):
        return li + 1

    @staticmethod
    def _list_index(hi):
        return hi - 1

    @staticmethod
    def _parent_index(hi):
        return hi // 2

    @staticmethod
    def _left_child_index(hi):
        return hi * 2

    @staticmethod
    def _right_child_index(hi):
        return 2 * hi + 1

    def _has_child(self, hi):
        return self._left_child_index(hi) <= len(self)

    def _has_right_child(self, hi):
        return self._right_child_index(hi) <= len(self)

    def _swap(self, hi, hj):
        li = self._list_index(hi)
        lj = self._list_index(hj)
        if li < 0 or li >= len(self) or lj < 0 or lj >= len(self):
            IndexError('Argument is out of bounds')
        temp = self._list[li]
        self._list[li] = self._list[lj]
        self._list[lj] = temp

    def push(self, key):
        self._list.append(key)

    def pop(self):
        return self._list.pop(0)

    def peak(self):
        if len(self._list) >= 1:
            return self._list[0]
        return None


class OrderedHeap(Heap):
    __metaclass__ = ABCMeta

    def __init__(self, array=None):
        super(OrderedHeap, self).__init__(array)
        for i in range(1, len(self._list)):
            self._heapify(i)

    def _heapify(self, hi):
        if hi < 1 or hi > len(self):
            ValueError('Index out of bounds')
        if not self._has_child(hi):
            return
        heapier_child_index = self._left_child_index(hi)
        if self._has_right_child(hi):
            heapier_child_index = self._heapier(self._left_child_index(hi), self._right_child_index(hi))
        heapiest = self._heapier(hi, heapier_child_index)
        if hi is heapiest:
            return
        else:
            self._swap(hi, heapier_child_index)
            if hi is not 1:
                self._heapify(self._parent_index(hi))

    @abstractmethod
    def _heapier(self, hi, hj):
        pass

    def push(self, key):
        super(OrderedHeap, self).push(key)
        self._heapify(self._parent_index(len(self)))

    def pop(self):
        self._swap(1, len(self))
        key = self._list.pop(self._list_index(len(self)))
        self._heapify(1)
        return key
