class _MyQueueNode(object):
    def __init__(self, key):
        self._key = key
        self.next = None
        self.previous = None

    @property
    def key(self):
        return self._key


class MyQueue(object):
    def __init__(self, iterable=None, type_restriction=None):
        self._length = 0
        self._head = None
        self._tail = self._head
        self._type_restriction = type_restriction
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __len__(self):
        return self._length

    @property
    def type_restriction(self):
        return self._type_restriction

    def push(self, key):
        if self._type_restriction is not None and type(key) is not self._type_restriction:
            return False
        node = _MyQueueNode(key)
        if self._head is None:
            self._head = node
            self._tail = self._head
        else:
            self._tail.next = node
            node.previous = self._tail
            self._tail = node
        self._length += 1
        return True

    def pop(self):
        if self._head is None:
            raise KeyError('Cannot pop from empty queue')
        ret = self._head.key
        if self._head.next is not None:
            self._head.next.previous = False
        else:
            self._tail = None
        self._head = self._head.next
        self._length -= 1
        return ret

    def peak(self):
        if self._head is not None:
            return self._head.key
        return None
