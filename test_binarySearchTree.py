from unittest import TestCase
from BinarySearchTree import BinarySearchTree
import random


class TestBinarySearchTree(TestCase):
    def test_construction(self):
        bst1 = BinarySearchTree()
        bst2 = BinarySearchTree(allow_duplicates=False)
        bst2 = BinarySearchTree(type_restriction=int)
        list1 = [random.randint(0, 100) for i in range(0, 100)]
        bst3 = BinarySearchTree(list1)
        bst4 = BinarySearchTree(list1, type_restriction=int)
        try:
            bst5 = BinarySearchTree(list1, type_restriction=str)
        except TypeError:
            pass  # expected code path
        else:
            return self.fail('BST cstor created tree of ints despite being a str tree')
        distinct_list1 = list(set(list1))
        bst6 = BinarySearchTree(distinct_list1, allow_duplicates=True)

    def test_insert(self):
        bst1 = BinarySearchTree()
        try:
            bst1.insert(None)
        except KeyError:
            pass  # expected code path
        else:
            return self.fail('BST.insert allowed a None key')
        if not bst1.insert(0):
            return self.fail('BST.insert did not return True, but should have')
        if len(bst1) != 1:
            return self.fail('BST.insert did not increment length')
        bst1.insert(2)
        bst1.insert(1.0)
        if bst1._root.key != 0 or bst1._root.right.key != 2 or bst1._root.right.left.key != 1.0:
            return self.fail('BST.insert did not build tree in predicted fashion')
        bst2 = BinarySearchTree(type_restriction=int)
        bst2.insert(0)
        bst2.insert(2)
        try:
            bst2.insert('string')
        except TypeError:
            pass  # expected code path
        else:
            return self.fail('BST.insert allowed insertion of string to an int tree')
        bst3 = BinarySearchTree(allow_duplicates=False)
        bst3.insert(0)
        if bst3.insert(0):
            return self.fail('BST.insert return True when inserting a disallowed duplicate')
        if len(bst3) > 1:
            return self.fail('BST.insert incremented len when inserting disallowed duplicate')
        if bst3._root.left is not None or bst3._root.right is not None:
            return self.fail('BST.insert added a new node for a duplicate value, but should not have')
        list1 = [8, 4, 12, 2, 6, 10, 14]
        bst4 = BinarySearchTree()
        for i in list1:
            bst4.insert(i)
        found_error = False
        found_error = found_error or bst4._root is None
        found_error = found_error or bst4._root.key != 8
        found_error = found_error or bst4._root.left is None
        found_error = found_error or bst4._root.left.key != 4
        found_error = found_error or bst4._root.left.left is None
        found_error = found_error or bst4._root.left.left.key != 2
        found_error = found_error or bst4._root.left.right is None
        found_error = found_error or bst4._root.left.right.key != 6
        found_error = found_error or bst4._root.right is None
        found_error = found_error or bst4._root.right.key != 12
        found_error = found_error or bst4._root.right.left is None
        found_error = found_error or bst4._root.right.left.key != 10
        found_error = found_error or bst4._root.right.right is None
        found_error = found_error or bst4._root.right.right.key != 14
        if found_error:
            return self.fail('BST.insert did not build the expected tree')

    def test_remove(self):
        bst1 = BinarySearchTree()
        try:
            bst1.remove(0)
        except KeyError:
            pass  # expected code path
        else:
            return self.fail('BST.remove did not raise error on key not in tree')
        bst1.insert(3)
        bst1.remove(3)
        if bst1._root is not None:
            return self.fail('BST.remove did not eliminate root node from single-entry tree')
        if len(bst1) != 0:
            return self.fail('BST.remove did not decrement length')
        list1 = [8, 4, 12, 6, 2, 10, 14]
        for element in list1:
            bst1.insert(element)
        try:
            bst1.remove(1)
        except KeyError:
            pass  # expected code pass
        else:
            return self.fail('BST.remove did not throw error when passed a bad key, but should have')
        bst1.remove(14)
        if bst1._root.right.right is not None:
            return self.fail('BST.remove did not remove the leaf node with the specified key')
        bst1.remove(4)
        if bst1._root.left.key == 4 or (bst1._root.left.left is not None and bst1._root.left.right is not None):
            return self.fail('BST.remove did not remove the branch node with the specified key')
        bst1.remove(8)
        if bst1._root.key == 8:
            return self.fail('BST.remove did not remove the root node')
        bst2 = BinarySearchTree(list1)
        bst2.insert(10)
        bst2.remove(10)
        if not bst2.contains(10):
            return self.fail('BST.remove eliminated all values in tree (or duplicate was not inserted)')
        bst3 = BinarySearchTree()
        list2 = self.perfect_binary_list(4)
        for item in list2:
            bst3.insert(item)
        bst3.remove(list2[-1])
        list2.remove(list2[-1])
        for item in list2:
            if not bst3.contains(item):
                self.fail('BST.remove removed more than just a leaf')
        # TODO middle node and root node
        bst3.remove(list2[3])
        list2.remove(list2[3])
        for item in list2:
            if not bst3.contains(item):
                self.fail('BST.remove removed or than just a tier 2 node')
        bst3.remove(list2[0])
        list2.remove(list2[0])
        for item in list2:
            if not bst3.contains(item):
                self.fail('BST.remove removed or than just the root node')


    def test_remove_all(self):
        bst1 = BinarySearchTree(allow_duplicates=False)
        list1 = [8, 4, 12, 2, 6, 10, 14]
        for i in list1:
            bst1.insert(i)
        bst1.remove_all(4)
        if bst1._root.left.key == 4:
            return self.fail('BST.remove_all did not remove the specified key')
        if len(bst1) != len(list1)-1:
            return self.fail('BST.remove_all did not decrement length at all')
        bst2 = BinarySearchTree(allow_duplicates=True)
        for i in list1:
            bst2.insert(i)
        bst2.insert(4)
        bst2.insert(8)
        bst2.remove_all(4)
        if bst2.contains(4):
            return self.fail('BST.remove_all did not remove all instances of the specified key')
        if len(bst2) != len(list1):
            return self.fail('BST.remove_all did not decrement length enough when removing multiple keys')
        bst2.remove_all(8)
        if bst2._root.key == 8 or bst2.contains(8):
            return self.fail('BST.remove_all did note remove all instances of root key')
        length = len(bst2)
        bst2.remove_all(4)
        if len(bst2) != length:
            return self.fail('BST.remove_all decremented length, but should not have had any effect')

    def test_contains(self):
        tree = BinarySearchTree(self.perfect_binary_list(5))
        if not tree.contains(16):
            return self.fail('BST.contains did not find root')
        if not tree.contains(7):
            return self.fail('BST.contains did not find leaf')
        if tree.contains(33):
            return self.fail('BST.contains found element not in tree')

    def test_mode(self):
        bst1 = BinarySearchTree(allow_duplicates=False)
        list1 = [8, 4, 12, 2, 6, 10, 14]
        for i in list1:
            bst1.insert(i)
        if bst1.mode(1) != 0:
            return self.fail('BST.mode returned non-zero for non-present value')

    def test_allow_duplicates(self):
        bst0 = BinarySearchTree()
        if not bst0._allow_duplicates:
            return self.fail('BST._allow_duplicates defaulted to False, but should not have')
        bst1 = BinarySearchTree(allow_duplicates=False)
        if bst1.allow_duplicates:
            return self.fail('BST allow_duplicates should be False but is not')
        bst1.insert(0)
        if bst1.insert(0):
            return self.fail('BST allowed duplicates, but should not have')
        bst2 = BinarySearchTree(allow_duplicates=True)
        if not bst2.allow_duplicates:
            return self.fail('BST allow_duplicates should be True but is not')
        bst2.insert(0)
        try:
            bst2.insert(0)
        except ValueError:
            return self.fail('BST did not allow duplicate, but should have')

    def test_minimum(self):
        tree1 = BinarySearchTree()
        try:
            x = tree1.minimum
        except ValueError:
            pass  # expected code path
        else:
            self.fail('BST.minimum did not raise a value error on an empty tree')
        tree1.insert(2)
        if tree1.minimum != 2:
            self.fail('BST.minimum did not return the root of a single-element tree')
        tree1.insert(3)
        if tree1.minimum != 2:
            self.fail('BST.minimum failed to return root, when it was the minimum')
        tree2 = BinarySearchTree(self.perfect_binary_list(5))
        if tree2.minimum != 1:
            self.fail('BST.minimum did not return minimum of a filled tree')

    def test_maximum(self):
        tree1 = BinarySearchTree()
        try:
            x = tree1.maximum
        except ValueError:
            pass  # expected code path
        else:
            self.fail('BST.maximum did not raise a value error on an empty tree')
        tree1.insert(2)
        if tree1.maximum != 2:
            self.fail('BST.maximum did not return the root of a single-element tree')
        tree1.insert(1)
        if tree1.maximum != 2:
            self.fail('BST.maximum did not return the root, when it was the maximum')
        tree2 = BinarySearchTree(self.perfect_binary_list(5))
        if tree2.maximum != 31:
            self.fail('BST.maximum did not return maximum of a filled tree')

    def test_successor(self):
        tree1 = BinarySearchTree()
        try:
            tree1.successor(1)
        except KeyError:
            pass  # expected code path
        else:
            self.fail('BST.successor did not raise error on empty tree')
        tree1.insert(1)
        try:
            tree1.successor(0)
        except KeyError:
            pass  # expected code path
        else:
            self.fail('BST.successor did not raise error for bad key')
        if tree1.successor(1) is not None:
            self.fail('BST.successor did not return None for a single-element tree')
        tree1.insert(2)
        if tree1.successor(2) is not None:
            self.fail('BST.successor did not return None for maximum value in tree')
        tree2 = BinarySearchTree(self.perfect_binary_list(5))
        for i in range(1, 31):
            if tree2.successor(i) != i+1:
                self.fail('BST.successor did not return the successor in a filled tree')

    def test_predecessor(self):
        tree1 = BinarySearchTree()
        try:
            tree1.predecessor(1)
        except KeyError:
            pass  # expected code path
        else:
            self.fail('BST.predecessor did not raise error on empty tree')
        tree1.insert(1)
        try:
            tree1.predecessor(0)
        except KeyError:
            pass  # expected code path
        else:
            self.fail('BST.predecessor did not raise error for bad key')
        if tree1.predecessor(1) is not None:
            self.fail('BST.predecessor did not return None for a single-element tree')
        tree1.insert(0)
        if tree1.predecessor(0) is not None:
            self.fail('BST.predecessor did not return None for min value in tree')
        tree2 = BinarySearchTree(self.perfect_binary_list(5))
        for i in range(31, 1, -1):
            if tree2.predecessor(i) != i-1:
                self.fail('BST.predecessor did not return the predecessor in a filled tree')

    def test__rotate_left(self):
        tree1 = BinarySearchTree()
        tree1.insert(1)
        tree1.insert(2)
        tree1._root.rotate_left()
        if tree1._root.key != 2 or tree1._root.left is None or tree1._root.left.key != 1 or tree1._root.right is not None:
            self.fail('Rotating the root left failed')
        try:
            tree1._root.rotate_left()
        except AttributeError:
            pass  # expected code path
        else:
            self.fail('Somehow, rotating root left twice worked')
        tree2 = BinarySearchTree(self.perfect_binary_list(5))
        tree2._find(8).rotate_left()
        if not self.tree_is_sorted(tree2):
            self.fail('Rotating mid-level node left made tree no longer sorted')
        if tree2._root.left.key != 12 or tree2._root.left.left.key != 8 or tree2._root.left.right.key != 14:
            self.fail('Rotating mid-level node left went wrong')

    def test__rotate_right(self):
        tree1 = BinarySearchTree()
        tree1.insert(2)
        tree1.insert(1)
        tree1._root.rotate_right()
        if tree1._root.key != 1 or tree1._root.right is None or tree1._root.right.key != 2 or tree1._root.left is not None:
            self.fail('Rotating the root right failed')
        try:
            tree1._root.rotate_right()
        except AttributeError:
            pass  # expected code path
        else:
            self.fail('Somehow, rotating root right twice worked')
        tree2 = BinarySearchTree(self.perfect_binary_list(5))
        tree2._find(24).rotate_right()
        if not self.tree_is_sorted(tree2):
            self.fail('Rotating mid-level node right made tree no longer sorted')
        if tree2._root.right.key != 20 or tree2._root.right.right.key != 24 or tree2._root.right.left.key != 18:
            self.fail('Rotating mid-level node right went wrong')

    @staticmethod
    def tree_is_sorted(tree):
        if tree._root is None:
            return True
        return TestBinarySearchTree._node_is_sorted(tree._root)

    @staticmethod
    def _node_is_sorted(node):
        correct = True
        if node.left is not None and node.key < node.left.key:
            correct = False
        if node.right is not None and node.key > node.right.key:
            correct = False
        if correct:
            if node.left is not None:
                correct = TestBinarySearchTree._node_is_sorted(node.left)
            if node.right is not None:
                correct = correct and TestBinarySearchTree._node_is_sorted(node.right)
        return correct

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
