from AvlTree import AvlTree

tree = AvlTree()
list1 = [16, 8, 24, 4, 12, 20, 28, 2, 6, 10, 14, 18, 22, 26, 30, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29,
         31]
for item in list1:
    tree.insert(item)
tree.insert(1)
key = 1
print(tree.list(1.5, 16))
low = 1.4
high = 6.7
print("length of tree.list is {0}, tree.count returns {1}".format(len(tree.list(low, high)), tree.count(low, high)))
dummy = 1
