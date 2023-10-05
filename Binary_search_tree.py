class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.current = None

    def insert(self, value):

        # create a new node
        new_node = Node(value)

        # Ceck if its root node else add the new node as root
        if not self.root:
            self.root = new_node
            print("created root")
            return

        # else
        self.current = self.root
        while True:
            if value < self.current.value:
                if self.current.left is None:
                    # go left
                    self.current.left = new_node
                    break
                else:
                    self.current = self.current.left
            else:
                if self.current.right is None:
                    # go right
                    self.current.right = new_node
                    break
                else:
                    self.current = self.current.right
        print("Node added")
        return

    def lookup(self, value):
        self.current = self.root
        while True:
            if value == self.current.value:
                msg = "Value found"
                break
            elif value < self.current.value:
                if self.current.left is not None:
                    # go left
                    self.current = self.current.left
                else:
                    msg = "Value not found"
                    break
            else:
                if self.current.right is not None:
                    self.current = self.current.right
                else:
                    msg = "Value not found"
                    break
        return msg


def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        if level > 0:
            indent = "    " * (level - 1) + "|--- "
        else:
            indent = ""
        print(indent + prefix + str(root.value))
        if root.left is not None or root.right is not None:
            print_tree(root.left, level + 1, "L")
            print_tree(root.right, level + 1, "R")


mytree = BinarySearchTree()
mytree.insert(9)
mytree.insert(4)
mytree.insert(6)
mytree.insert(20)
mytree.insert(170)
mytree.insert(15)
mytree.insert(1)
print(mytree.lookup(100))
print_tree(mytree.root)
