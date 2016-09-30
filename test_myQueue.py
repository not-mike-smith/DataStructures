from unittest import TestCase
from MyQueue import MyQueue


class TestMyQueue(TestCase):
    def test_push(self):
        #
        # Test 1st insertion
        q0 = MyQueue()
        q0.push(0)
        if q0._head is None or q0._head.key != 0 or q0._head.previous is not None:
            self.fail('MyQueue.push failed to insert 1st node correctly')
        if q0._tail is not q0._head:
            self.fail('MyQueue.push failed to point tail to head for single insertion')
        #
        # Test 3 insertions
        q1 = MyQueue()
        list1 = [0, 1, 2]
        for i in list1:
            succeeded = q1.push(i)
            if not succeeded:
                self.fail('MyQueue.push returned false, but logically should not have')
            if len(q1) != i + 1:
                self.fail('MyQueue.push failed to increment length')
        if q1._head is None or q1._head.key != 0 or q1._head.previous is not None:
            self.fail('MyQueue.push failed to add 1st node correctly (twice!)')
        if q1._head.next is None or q1._head.next.key != 1 or q1._head.next.previous is not q1._head:
            self.fail('MyQueue.push failed to add 2nd node correctly')
        if q1._head.next.next is None or q1._head.next.next.key != 2 or\
                q1._head.next.next.previous is not q1._head.next or q1._head.next.next.next is not None:
            self.fail('MyQueue.push failed to add 3rd node correctly')
        if q1._tail is not q1._head.next.next:
            self.fail('MyQueue._tail is not pointed to the correct node')
        #
        # Test the type restriction
        q2 = MyQueue(type_restriction=int)
        for i in list1:
            succeeded = q2.push(i)
            if not succeeded:
                self.fail('MyQueue.push returned FALSE, but logically should not have (v2)')
        succeeded = q2.push('')
        if succeeded:
            self.fail('MyQueue.push returned TRUE when inserting string to int queue')
        if q2._tail.key == '':
            self.fail('MyQueue.push added an empty string to an int queue')
        if len(q2) != len(list1):
            self.fail('MyQueue.push incremented the length when pushing string to an int queue')

    def test_pop(self):
        #
        # Empty queue
        q0 = MyQueue()
        try:
            garbage = q0.pop()
        except KeyError:
            pass  # expected code path
        else:
            self.fail('MyQueue.pop did not raise error for empty queue')
        #
        # First element
        q0.push(0)
        value = q0.pop()
        if value != 0:
            self.fail('MyQueue.pop did not return 1st and only element in queue')
        if len(q0) != 0:
            self.fail('MyQueue.pop did not decrement length for 1st and only element in queue')
        if q0._head is not None or q0._tail is not None:
            self.fail('MyQueue.pop did not set null out head and tail for last element in queue')
        list1 = [0, 1, 2]
        for i in list1:
            q0.push(i)
        expected_length = len(list1)
        for i in list1:
            value = q0.pop()
            expected_length -= 1
            if value != i:
                self.fail('MyQueue.pop did not return value expected for {} item in list'.format(i))
            if len(q0) != expected_length:
                self.fail('MyQueue.pop did not decrement length.  It is {}, but should be {}'.format(len(q0),
                                                                                                     expected_length))

    def test_peak(self):
        q = MyQueue()
        if q.peak() is not None:
            self.fail('MyQueue.peak did not return null for empty queue')
        q.push(0)
        if q.peak() != 0:
            self.fail('MyQueue.peak did not return root for single element queue')
        q.push(1)
        if q.peak() != 0:
            self.fail('MyQueue.peak did not return root for 2 element queue')
        q.pop()
        if q.peak() != 1:
            self.fail('MyQueue.peak did not return root after a pop')

    def test_construction(self):
        q0 = MyQueue()
        q1 = MyQueue([])
        # if q0 != q1:
        #     self.fail('MyQueue init by empty list is different from init with nothing')
        list1 = [0, 1, 2]
        q2 = MyQueue(list1)
        q3 = MyQueue()
        for i in list1:
            q3.push(i)
        while q2.peak() is not None and q3.peak() is not None:
            if q2.pop() != q3.pop():
                self.fail('MyQueue init by list is different from MyQueue where list was pushed')
        if len(q2) != len(q3):
            self.fail('MyQueue init by list is different from MyQueue where list was pushed')
        q4 = MyQueue(type_restriction=int)
        for i in list1:
            q4.push(i)
        if q4._type_restriction is not int:
            self.fail('MyQueue init with a type restriction did not seem to stick')
