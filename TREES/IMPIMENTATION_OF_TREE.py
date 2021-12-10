
class Binary_tree(object):

    def __init__(self,root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left_child(self,value):
        if self.left_child == None:
            self.left_child = Binary_tree(value)

        else:
            t = Binary_tree(value)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right_child(self, value):
        if self.right_child == None:
            self.right_child = Binary_tree(value)

        else:
            t = Binary_tree(value)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def root_value(self):
        return self.key

    def set_root_value(self,value):
        self.key = value


tree = Binary_tree('a')
tree.insert_left_child('b')
tree.insert_left_child('d')
tree.insert_right_child('e')

tree.insert_right_child('c')
tree.insert_left_child('f')
tree.insert_right_child('g')


def treverse_tree(tree):

    if tree:
        print(tree.root_value())
        treverse_tree(tree.get_left_child())
        treverse_tree(tree.get_right_child())

treverse_tree(tree)




