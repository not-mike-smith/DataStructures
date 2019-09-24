def listOfIterable(iterable):
    if iterable is None:
        return []
    return list(iterable)

def raiseErrorIfTypeMismatch(type_restriction, item):
    if (type_restriction is None):
        return
    if type(item) is not type_restriction:
        raise TypeError('Iterable elements are not of type {}'.format(type_restriction))

class Stack(object):
    def __init__(self, iterable=None, type_restriction=None):
        self._list = listOfIterable(iterable)
        self._type_restriction = type_restriction
        map(lambda i: raiseErrorIfTypeMismatch(self._type_restriction, i), self._list)

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
