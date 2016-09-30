from AvlTree import AvlTree
from _RankedAvlNode import RankedAvlNode


class RankedAvlTree(AvlTree):
    def __init__(self, iterable=None, allow_duplicates=True, type_restriction=None):
        super(RankedAvlTree, self).__init__(iterable, allow_duplicates, type_restriction)

    def insert(self, key):
        if not self._can_insert(key):
            return False
        node = RankedAvlNode(key, self)
        self._insert(node)
        node.update_sizes(1)
        node.update_height_and_rebalance()
        return True

    def _remove(self, dead_node):
        parent = self._remove_and_return_parent(dead_node)
        if parent is not None:
            parent.update_sizes(-1)
        self._rebalance_after_removal(parent)

    def rank(self, key):
        """
        :param key: key which may exist in tree
        :return: int rank of first instance of key in tree, or None if key does not exist in tree
        """
        node = self._root
        if node is None:
            return None
        rank = node.get_size(node.left)
        while node is not None and node.key != key:
            if key < node.key:
                node = node.left
                if node is not None:
                    rank -= 1 + node.get_size(node.right)
            else:
                node = node.right
                if node is not None:
                    rank += 1 + node.get_size(node.left)
        if node is None:
            return None
        if self._allow_duplicates:
            predecessor = node.predecessor()
            while predecessor is not None and predecessor.key == key:
                # node = predecessor
                predecessor = predecessor.predecessor()
                rank -= 1
        return rank

    def __getitem__(self, item):
        if item >= len(self) or item < -len(self):
            raise IndexError('Index out of range')
        if item < 0:
            item += len(self)
        node = self._root
        rank = node.get_size(node.left)
        while rank != item:
            if item < rank:
                node = node.left
                rank -= 1 + node.get_size(node.right)
            else:
                node = node.right
                rank += 1 + node.get_size(node.left)
        return node.key
