""" Nodes of a tree contain three main elements: references to left and right nodes and a value (data) """
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    """ Conveniently determines whether there is a node at the left of this one """
    def is_left_empty(self)->bool:
        return self.left is None

    """ Conveniently determines whether there is a node at the right of this one """
    def is_right_empty(self)->bool:
        return self.right is None

class BinaryTree:
    def __init__(self, root:Node = None):
        self.root = root

    """ Add a new node to the tree """
    def add(self, data):
        if self.root is None:
            self.root = Node(data)

        current_pos = self.root

        while True:
            if data < current_pos.data:
                if current_pos.is_left_empty():
                    current_pos.left = Node(data)
                    break
                else:
                    current_pos = current_pos.left

            elif data > current_pos.data:
                if current_pos.is_right_empty():
                    current_pos.right = Node(data)
                    break
                else:
                    current_pos = current_pos.right
            else:
                # Trying to add a node with an existing value, ignore it
                return

    """ Search for a node with a given value -> O(logN) """
    def find(self, data)->Node:
        current_pos = self.root

        while current_pos is not None:
            if data < current_pos.data:
                current_pos = current_pos.left
            elif data > current_pos.data:
                current_pos = current_pos.right
            else:
                return current_pos

        return None

    """
    Not yet implemented
    def delete(self, data, start_node:Node = None)->bool:
        if start_node is None:
            return start_node

        if data < start_node.data:
            # Move to the left sub-tree
            start_node.left = self.delete(data, start_node.left)
        elif data > start_node.data:
            # Move to the right sub-tree
            start_node.right = self.delete(data, start_node.right)
        else:
            if start_node.is_left_empty():
                t = start_node.right
                t = None
                return t

            elif start_node.is_right_empty():
                t = start_node.left
                t = Node
                return t

    """

    """ Traverse the tree in-order (Left -> Root -> Right) """
    def traverse_in_order(self, start_node:Node = None):
        t = []
        
        if start_node:
            t = self.traverse_in_order(start_node.left)
            t.append(start_node.data)
            t = t + self.traverse_in_order(start_node.right)

        return t

    """ Traverse the tree pre-order """
    # def traverse_pre_order(self, start_node:Node = None):

if __name__ == "__main__":
    
    """ Initialise tree with root node value = 2 """
    tree = BinaryTree(Node(2))

    tree.add(5)
    tree.add(3)
    tree.add(1)
    tree.add(8)
    tree.add(6)
    tree.add(10)
    tree.add(7)
    tree.add(15)
    tree.add(9)

    print(tree.traverse_in_order(tree.root))

    """ Replace 7 with another value and see the output """
    print(f'Search for 7: {tree.find(7) and tree.find(7).data}')