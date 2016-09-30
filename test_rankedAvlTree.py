from unittest import TestCase
from random import Random
from RankedAvlTree import RankedAvlTree


class TestRankedAvlTree(TestCase):
    def test_count(self):
        tree1 = RankedAvlTree()
        if tree1.count(0, 0) != 0:
            self.fail('RankedAvlTree.count failed on empty tree')
        tree1.insert(1)
        if tree1.count(0, 2) != 1:
            self.fail('RankedAvlTree.count failed with single node')
        if tree1.count(-1, 0) != 0:
            self.fail('RankedAvlTree.count failed with single node greater than high bound')
        if tree1.count(2, 3) != 0:
            self.fail('RankedAvlTree.count failed with single node less than lower bound')
        if tree1.count(1, 1) != 1:
            self.fail('RankedAvlTree.count failed with single node equal to both bounds')
        if tree1.count(1, 5) != 1:
            self.fail('RankedAvlTree.count failed with single node equal to lower bound')
        if tree1.count(-3, 1) != 1:
            self.fail('RankedAvlTree.count failed with single node equal to higher bound')
        tree1.insert(2)
        if tree1.count(1, 2) != 2:
            self.fail('RankedAvlTree.count failed with two nodes, equal to both bounds')
        tree1.insert(0)
        tree1.insert(1)
        if tree1.count(1, 1) != 2:
            self.fail('RankedAvlTree.count failed on duplicates, equal to both bounds')
        if tree1.count(0.5, 1.5) != 2:
            self.fail('RankedAvlTree.count failed on duplicates, compare floats to ints')
        if tree1.count(1.5, 0.5) != 2:
            self.fail('RankedAvlTree.count failed with bounds switched')
        if tree1.count(0.5, 0.6) != 0:
            self.fail('RankedAvlTree.count failed with bounds too tight')
        tree2 = RankedAvlTree(self.perfect_binary_list(5))
        if tree2.count(0, 1000) != len(tree2):
            self.fail('RankedAvlTree.count failed with large tree with entire tree within bounds')
        tree2.remove(1)
        tree2.remove(12)
        tree2.remove(24)
        tree2.remove(16)
        if tree2.count(0, 1000) != len(tree2):
            self.fail('RankedAvlTree.count failed with large tree after some deletions with entire tree within bounds')
        if tree2.count(0, 11) != 10:
            self.fail('RankedAvlTree.count failed in lower end of large tree after deletions')
        if tree2.count(0, 16) != 13:
            self.fail('RankedAvlTree.count failed, attempt 1')
        if tree2.count(14.5, 17.5) != 2:
            self.fail('RankedAvlTree.count failed, attempt 2')
        if tree2.count(13, 14) != 2:
            self.fail('RankedAvlTree.count failed, attempt 3')
        if tree2.count(13, 17) != 4:
            self.fail('RankedAvlTree.count failed, attempt 4')

    def test_rank(self):
        rand = Random()
        list1 = [rand.randint(0, 100000) for i in range(0, 1024)]
        list1 = list(set(list1))
        tree1 = RankedAvlTree(list1)
        list1.sort()
        errors = []
        for element in list1:
            if list1[tree1.rank(element)] != element:
                errors.append((element, tree1.rank(element)))
        if len(errors) != 0:
            self.fail('RankedAvlTree.rank failed')
        if tree1.rank(-1) is not None:
            self.fail('RankedAvlTree.rank failed to return None for key not in tree')
        tree2 = RankedAvlTree()
        if tree2.rank(0) is not None:
            self.fail('RankedAvlTree.rank failed to return None on empty tree')
        tree2.insert(1)
        tree2.insert(1)
        tree2.insert(1)
        if tree2.rank(1) != 0:
            self.fail('RankedAvlTree.rank failed to return rank of first element in tree')

    def test_get_item(self):
        rand = Random()
        list1 = [rand.randint(0, 100) for i in range(0, 255)]
        tree1 = RankedAvlTree(list1)
        list1.sort()
        error_list = []
        for i in range(-len(list1), len(list1)):
            if tree1[i] != list1[i]:
                error_list.append((i, list1[i], tree1[i]))
        if len(error_list) != 0:
            self.fail('RankedAvlTree.__getitem__ failed to return correct value')
        tree2 = RankedAvlTree()
        try:
            dummy = tree2[0]
        except IndexError:
            pass  # expected code path
        else:
            self.fail('RankedAvlTree.__getitem__ failed to raise index error on empty tree')
        tree2.insert(0)
        try:
            dummy = tree2[1]
        except IndexError:
            pass  # expected code path
        else:
            self.fail('RankedAvlTree.__getitem__ failed to raise index error for too-positive number')
        try:
            dummy = tree2[-2]
        except IndexError:
            pass  # expected code path
        else:
            self.fail('RankedAvlTree.__getitem__ failed to raise index error for too-negative number')

    @staticmethod
    def perfect_binary_list(height):
        ret = [1]
        for count in range(1, height):
            ret = [i*2 for i in ret]
            j = 1
            while j < 2 * ret[0]:
                ret.append(j)
                j += 2
        return ret
