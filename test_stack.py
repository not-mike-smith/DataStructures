from unittest import TestCase
from Stack import Stack


class TestStack(TestCase):
    def test_push(self):
        s = Stack()
        s.push(0)
        if len(s) != 1:
            return self.fail('Stack.push did not increment length')
        s = Stack(type_restriction=int)
        s.push(0)
        if len(s) != 1:
            return self.fail('Stack.push did not add an int')
        try:
            s.push('')
        except TypeError:
            pass
        else:
            return self.fail('An int Stack allowed a string')

    def test_peak(self):
        s = Stack([6, 4, 3, 0])
        if s.peak() != 0:
            return self.fail('Stack either did not make it from the provided list, or peak failed')
        if len(s) != 4:
            return self.fail('Stack.peak seems to have popped')

    def test_pop(self):
        s = Stack([6, 4, 3, 0])
        if s.pop() != 0:
            return self.fail('Stack either did not make it from the provided list, or pop failed')
        if len(s) != 3:
            return self.fail('Stack.pop did not decrement length')

    def test_construction(self):
        l = [0, 1, 2, 3]
        s = Stack(l)
        if len(s) != 4:
            return self.fail('Stack construction from a list failed')
        i = len(s) - 1
        while i >= 0:
            if s.pop() != l[i]:
                return self.fail('Stack construction from a list failed')
            i -= 1
        s = Stack(l, type_restriction=int)
        if len(s) != 4:
            return self.fail('Stack construction from list with type construction failed')
        try:
            s = Stack([''], type_restriction=int)
        except TypeError:
            pass  # expected code path
        else:
            return self.fail('Stack allowed construction from list of strings with int type_restriction')
