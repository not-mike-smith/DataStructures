from _BstNode import BstNode


class AvlNode(BstNode):
    def __init__(self, key, tree):
        super(AvlNode, self).__init__(key, tree)
        self._height = None

    @property
    def height(self):
        return self._height

    @staticmethod
    def get_height(node):
        if node is not None:
            return node.height
        else:
            return 0

    def update_height_and_rebalance(self):
        if self.update_height() and self.parent is not None:
            if not self.parent.is_balanced():
                self.parent.rebalance()
            else:
                self.parent.update_height_and_rebalance()

    def update_height(self):
        new_height = 1 + max(AvlNode.get_height(self.left), AvlNode.get_height(self.right))
        if new_height == self._height:
            return False
        self._height = new_height
        return True

    def is_balanced(self):
        return abs(self.get_height(self.left) - self.get_height(self.right)) < 2

    def rebalance_left(self):
        if AvlNode.get_height(self.left.left) < AvlNode.get_height(self.left.right):
            self.left.rotate_left()
            self.left.left.update_height()
        self.rotate_right()

    def rebalance_right(self):
        if AvlNode.get_height(self.right.right) < AvlNode.get_height(self.right.left):
            self.right.rotate_right()
            self.right.right.update_height()
        self.rotate_left()

    def rebalance(self):
        if self.get_height(self.left) > self.get_height(self.right):
            self.rebalance_left()
        else:
            self.rebalance_right()
        self.update_height_and_rebalance()  # will force parent to update
        if self.parent.parent is not None:
            self.parent.parent.update_height_and_rebalance()

    def swap(self, node):
        super(AvlNode, self).swap(node)
        node.update_height()
        self.update_height()