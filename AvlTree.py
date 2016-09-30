from BinarySearchTree import BinarySearchTree
from _AvlNode import AvlNode


class AvlTree(BinarySearchTree):
    def __init__(self, iterable=None, allow_duplicates=True, type_restriction=None):
        super(AvlTree, self).__init__(iterable, allow_duplicates, type_restriction)

    def insert(self, key):
        if not self._can_insert(key):
            return False
        node = AvlNode(key, self)
        self._insert(node)
        node.update_height_and_rebalance()
        return True

    def _remove(self, dead_node):
        parent = self._remove_and_return_parent(dead_node)
        self._rebalance_after_removal(parent)

    @staticmethod
    def _rebalance_after_removal(node):
        while node is not None:
            if not node.is_balanced():
                node.rebalance()
                node = node.parent.parent
            elif node.update_height():
                node = node.parent
            else:
                node = None

    @property
    def height(self):
        return self._get_height(self._root)

    @staticmethod
    def _get_height(node):
        if node is None:
            return 0
        return node.height
