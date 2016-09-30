class BstNode(object):
    def __init__(self, key, tree):
        self._key = key
        self._tree = tree
        self._parent = None
        self._left = None
        self._right = None

    @property
    def key(self):
        return self._key

    @property
    def parent(self):
        return self._parent

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    def assign_left(self, node):
        self._left = node
        if node is not None:
            node._parent = self

    def assign_right(self, node):
        self._right = node
        if node is not None:
            node._parent = self

    @staticmethod
    def assign_root(tree, node):
        tree._root = node
        if node is not None:
            node._parent = None

    def disconnect(self):
        self._key = None
        self._tree = None
        self._parent = None
        self._left = None
        self._right = None

    def transplant(self, moved_node):
        if self.parent is None:
            BstNode.assign_root(self._tree, moved_node)
        elif self is self.parent.left:
            self.parent.assign_left(moved_node)
        else:
            self.parent.assign_right(moved_node)

    def swap(self, node):
        if node is None:
            raise ValueError('Cannot swap with None node')
        dummy = BstNode(None, self._tree)
        self.transplant(dummy)
        dummy.assign_left(self.left)
        dummy.assign_right(self.right)
        node.transplant(self)
        self.assign_left(node.left)
        self.assign_right(node.right)
        dummy.transplant(node)
        node.assign_left(dummy.left)
        node.assign_right(dummy.right)

    def rotate_left(self):
        new_subtree_root = self.right
        self.transplant(new_subtree_root)
        self.assign_right(new_subtree_root.left)
        new_subtree_root.assign_left(self)

    def rotate_right(self):
        new_subtree_root = self.left
        self.transplant(new_subtree_root)
        self.assign_left(new_subtree_root.right)
        new_subtree_root.assign_right(self)

    def far_left(self):
        node = self
        while node.left is not None:
            node = node.left
        return node

    def far_right(self):
        node = self
        while node.right is not None:
            node = node.right
        return node

    def successor(self):
        if self.right is not None:
            return BstNode.far_left(self.right)
        parent = self.parent
        node = self
        while parent is not None and node is parent.right:
            node = parent
            parent = node.parent
        return parent

    def predecessor(self):
        if self.left is not None:
            return BstNode.far_right(self.left)
        parent = self.parent
        node = self
        while parent is not None and node is parent.left:
            node = parent
            parent = node.parent
        return parent