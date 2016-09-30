from _AvlNode import AvlNode


class RankedAvlNode(AvlNode):
    def __init__(self, key, tree):
        super(RankedAvlNode, self).__init__(key, tree)
        self._size = 0

    @property
    def size(self):
        return self._size

    def update_sizes(self, delta):
        self._size += delta
        if self.parent is not None:
            self.parent.update_sizes(delta)

    def update_size(self):
        self._size = 1 + self.get_size(self.left) + self.get_size(self.right)

    @staticmethod
    def get_size(node):
        if node is None:
            return 0
        return node.size

    def rotate_left(self):
        new_subtree_root = self.right
        self.transplant(new_subtree_root)
        self.assign_right(new_subtree_root.left)
        new_subtree_root.assign_left(self)
        self.update_size()
        self.parent.update_size()

    def rotate_right(self):
        new_subtree_root = self.left
        self.transplant(new_subtree_root)
        self.assign_left(new_subtree_root.right)
        new_subtree_root.assign_right(self)
        self.update_size()
        self.parent.update_size()

    def swap(self, node):
        super(RankedAvlNode, self).swap(node)
        if node.parent is self:
            node.update_size()
            self.update_size()
        else:
            self.update_size()
            node.update_size()