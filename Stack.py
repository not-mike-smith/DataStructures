class Stack(object):
    def __init__(self, iterable=None, type_restriction=None):
        if iterable is None:
            self._list = []
        else:
            self._list = list(iterable)
        self._type_restriction = type_restriction
        if self._type_restriction is not None:
            for item in self._list:
                if type(item) is not self._type_restriction:
                    raise TypeError('Iterable elements are not of type {}'.format(self._type_restriction))

    def push(self, value):
        if self._type_restriction is not None and type(value) is not self._type_restriction:
            raise TypeError('Cannot add item because it is not of type {}'.format(self._type_restriction))
        self._list.append(value)

    def peak(self):
        if len(self._list) > 0:
            return self._list[-1]
        else:
            return None

    def pop(self):
        return self._list.pop()

    def __len__(self):
        return len(self._list)

    def __iter__(self):
        for item in self._list:
            yield item
