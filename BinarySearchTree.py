from _BstNode import BstNode


class BinarySearchTree(object):
    def __init__(self, iterable=None, allow_duplicates=True, type_restriction=None):
        self._root = None
        self._length = 0
        self._allow_duplicates = allow_duplicates
        self._type_restriction = type_restriction
        if iterable is not None:
            for item in iterable:
                self.insert(item)

    def __len__(self):
        return self._length

    def insert(self, key):
        if not self._can_insert(key):
            return False
        node = BstNode(key, self)
        self._insert(node)
        return True
    
    def _can_insert(self, key):
        if key is None:
            raise KeyError('Cannot insert None to tree')
        if self._type_restriction is not None and type(key) is not self._type_restriction:
            raise TypeError('Key, {}, is not of type {}'.format(key, self._type_restriction))
        if (not self._allow_duplicates) and self.contains(key):
            return False
        return True

    def _insert(self, node):
        if node is None:
            raise ValueError('Internal error: Cannot insert None node')
        self._length += 1
        previous = None
        current = self._root
        while current is not None:
            previous = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right
        if previous is None:
            BstNode.assign_root(self, node)
        elif node.key < previous.key:
            previous.assign_left(node)
        else:
            previous.assign_right(node)

    def remove(self, key):
        node = self._findOrRaiseError(key)
        self._remove(node)

    def remove_all(self, key):
        node = self._find(key)
        while node is not None:
            self._remove(node)
            node = self._find(key)

    def _remove(self, node):
        self._remove_and_return_parent(node)

    def _remove_and_return_parent(self, dead_node):
        if dead_node is None:
            raise ValueError('Cannot remove a None node')
        ret = dead_node.parent
        if dead_node.left is None:
            dead_node.transplant(dead_node.right)
        elif dead_node.right is None:
            dead_node.transplant(dead_node.left)
        else:
            dead_node.swap(dead_node.right.far_left())
            return self._remove_and_return_parent(dead_node)
        dead_node.disconnect()
        self._length -= 1
        return ret

    def contains(self, key):
        return self._find(key) is not None

    def mode(self, key):
        node = self._find(key)
        if node is None:
            return 0
        elif not self.allow_duplicates:
            return 1
        else:
            mode = 1
            temp = node.predecessor()
            while temp is not None and temp.key == key:
                mode += 1
                temp = temp.predecessor()
            temp = node.successor()
            while temp is not None and temp.key == key:
                mode += 1
                temp = temp.successor()
            return mode

    @property
    def allow_duplicates(self):
        return self._allow_duplicates

    @property
    def minimum(self):
        try:
            return self._root.far_left().key
        except:
            raise ValueError('Cannot return minimum of empty tree')

    @property
    def maximum(self):
        try:
            return self._root.far_right().key
        except:
            raise ValueError('Cannot return maximum of an empty tree')

    def _find(self, key):
        """
        :param key: key you want to find
        :return: first node with that key as its key; None if the key isn't in this tree
        """
        node = self._root
        while node is not None and node.key != key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node

    def _findOrRaiseError(self, key):
        node = self._find(key)
        if node is None:
            raise KeyError('Cannot find key, {}'.format(key))
        return node

    @staticmethod
    def _getKeyOrNone(node):
        if node is None:
            return None
        return node.key

    def successor(self, key):
        node = self._findOrRaiseError(key)
        node = node.successor()
        while self.allow_duplicates and node is not None and node.key == key:
            node = node.successor()
        return self._getKeyOrNone(node)

    def predecessor(self, key):
        node = self._findOrRaiseError(key)
        node = node.predecessor()
        while self.allow_duplicates and node is not None and node.key == key:
            node = node.predecessor()
        return self._getKeyOrNone(node)

    def list(self, first_key, last_key):
        list_builder = _ListBuilder(first_key, last_key)
        list_builder.build_list(self._root)
        return list_builder.list

    def count(self, first_key, last_key):
        return len(self.list(first_key, last_key))


class _ListBuilder(object):
    def __init__(self, lower_bound, higher_bound):
        if higher_bound < lower_bound:
            temp = higher_bound
            higher_bound = lower_bound
            lower_bound = temp
        self.lower_bound = lower_bound
        self.higher_bound = higher_bound
        self.list = []

    def build_list(self, node):
        if node is None:
            return
        if node.key < self.lower_bound:
            self.build_list(node.right)
        elif node.key > self.higher_bound:
            self.build_list(node.left)
        else:
            self.list.append(node.key)
            self.build_list(node.left)
            self.build_list(node.right)
