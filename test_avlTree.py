from unittest import TestCase
from AvlTree import AvlTree
from _AvlNode import AvlNode
from random import Random
from test_binarySearchTree import TestBinarySearchTree
import math


class TestAvlTree(TestCase):
    def test_insert(self):
        rand = Random()
        list1 = [rand.randint(0, 1000) for i in range(0, 255)]
        list2 = [i for i in range(0, 100)]
        tree = AvlTree(allow_duplicates=True)
        count = 0
        for item in list1:
            tree.insert(item)
            count += 1
            if not self._tree_is_balanced(tree):
                msg = 'Tree is not balanced after {} insertions. Elements inserted were \n{}'.format(count, list1[0:count])
                self.fail(msg)
        return self.tree_is_correct(tree, '1000 insertions')

    def test_remove(self):
        rand = Random()
        list1 = [rand.randint(0, 100) for i in range(0, 1023)]
        tree = AvlTree(allow_duplicates=True)
        for item in list1:
            tree.insert(item)
        removals = list1[0::8]
        for item in removals:
            tree.remove(item)
        self.tree_is_correct(tree, '{0} insertions and {1} removals'.format(len(list1), len(removals)))
        for i in removals:
            list1.remove(i)
        if len(tree) != len(list1):
            self.fail('Length of AvlTree is wrong after {0} insertions and {1} removals'.format(len(list1),
                                                                                                len(removals)))
        missing_count = 0
        for item in list1:
            if not tree.contains(item):
                missing_count += 1
        if missing_count != 0:
            self.fail("AvlTree is missing {} additional items after 1000 insertions and 100 removals".format(
                missing_count))

    def test_height(self):
        list1 = self.perfect_binary_list(8)
        tree1 = AvlTree()
        if tree1.height != 0:
            self.fail('AvlTree.height is wrong right off the bat')
        for i in range(0, len(list1)):
            tree1.insert(list1[i])
            if tree1.height != math.ceil(math.log2(i+2)):
                self.fail('tree height is wrong after {} insertions'.format(i+1))
        tree2 = AvlTree()
        tree2.insert(list1[0])
        tree2.insert(list1[1])
        tree2.insert(list1[2])
        # etc. including remove

    @staticmethod
    def _tree_is_balanced(tree):
        if tree._root is None:
            return True
        return TestAvlTree._node_is_balanced(tree._root)
    
    @staticmethod
    def _node_is_balanced(node):
        correct = abs(AvlNode.get_height(node.left) - AvlNode.get_height(node.right)) < 2
        if correct:
            if node.left is not None:
                correct = correct and TestAvlTree._node_is_balanced(node.left)
            if node.right is not None:
                correct = correct and TestAvlTree._node_is_balanced(node.right)
        else:
            print(node.key)
        return correct

    def tree_is_correct(self, tree, state='undefined state'):
        if not TestBinarySearchTree.tree_is_sorted(tree):
            return self.fail('AvlTree is not sorted after {}'.format(state))
        if not self._tree_is_balanced(tree):
            return self.fail('AvlTree is not balanced after {}'.format(state))

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
