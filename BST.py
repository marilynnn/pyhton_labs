class Node:
    '''Элемент дерева'''
    def __init__(self, value):
        self.val = value
        self.l_child = None
        self.r_child = None

    def insert_child(self, value):
        if value < self.val:
                self.l_child = Node(value)
        elif value > self.val:
                self.r_child = Node(value)

    def has_l_child(self):
        if  self.l_child is not None:
            return True
        else:
            return False

    def has_r_child(self):
        if self.r_child is not None:
            return True
        else:
            return False

    def __iter__(self):
        if self.l_child is not None:
            yield from self.l_child
        yield self
        if self.r_child is not None:
            yield from self.r_child

    def __str__(self):
        return "{0}".format(self.val)


class BST:
    ''' Бинарное дерево поиска'''

    def __init__(self, root = None):
        self.root = root

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.__insert(self.root, value)

    def __insert(self, curr_node, value):
        if value < curr_node.val:
            if curr_node.has_l_child():
                self.__insert(curr_node.l_child, value)
            else:
                curr_node.insert_child(value)
        elif value > curr_node.val:
            if curr_node.has_r_child():
                self.__insert(curr_node.r_child, value)
            else:
                curr_node.insert_child(value)

    def __iter__(self):
        yield from self.root


tree = BST()
l = (10,8,9,7,4,5,6,1,2,3,3,3,3)
for i in l:
    tree.insert(i)
for i in tree:
    print(i)
