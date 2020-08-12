""" Nodes of a tree contain three main elements: references to left and right nodes and a value (data) """
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.parent = None
        self.data = data

    """ Conveniently determines whether there is a node at the left of this one """
    def is_left_empty(self)->bool:
        return self.left is None

    """ Conveniently determines whether there is a node at the right of this one """
    def is_right_empty(self)->bool:
        return self.right is None

    def set_data(self, new_data):
        self.data = new_data

    def __eq__(self, other)->bool:
        return self.data == other.data

    def __str__(self)->str:
        return f'Node data: {self.data}\nLeft: {self.left}\nRight: {self.right}\nParent: {self.parent}'

class BinaryTree:
    def __init__(self, root:Node = None):
        self.root = root

    """ Add a new node to the tree """
    def add(self, data)->bool:
        if self.root is None:
            self.root = Node(data)
            return True

        current_pos = self.root

        while True:
            if data < current_pos.data:
                if current_pos.is_left_empty():
                    new_node = Node(data)
                    new_node.parent = current_pos
                    current_pos.left = new_node
                    return True
                else:
                    current_pos = current_pos.left

            elif data > current_pos.data:
                if current_pos.is_right_empty():
                    new_node = Node(data)
                    new_node.parent = current_pos
                    current_pos.right = new_node
                    return True
                else:
                    current_pos = current_pos.right
            else:
                # Trying to add a node with an existing value, ignore it
                return False

        return False

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

    def delete(self, data, start_node:Node = None)->bool:
        if self.root is None:
            return False

        current_pos = self.root

        while True:
            if current_pos is None:
                # node to be deleted not found
                break
            elif current_pos.data < data:
                current_pos = current_pos.right
            elif current_pos.data > data:
                current_pos = current_pos.left
            else:
                # node to be deleted was found
                break

        if current_pos.data == data:
            if current_pos.is_left_empty() and not current_pos.is_right_empty():
                # current_pos.right replaces current_pos
                current_pos.right.parent = current_pos.parent
                # TODO: Connect current_pos.parent to current_pos.right or current_pos.left in the next case
                # Probably non-trivial
                current_pos = current_pos.right
            elif not current_pos.is_left_empty() and current_pos.is_right_empty():
                # current_pos.left replaces current_pos
                current_pos.left.parent = current_pos.parent
                current_pos = current_pos.left
            elif current_pos.is_left_empty() and current_pos.is_right_empty():
                # current_pos won't be missed!
                current_pos = None
            else:
                # did current_pos come from current_pos.parent.left or current_pos.parent.right?
                if current_pos.parent.left == current_pos:
                    # shift current_pos.left to current_pos
                    current_pos.left.parent = current_pos.parent
                    current_pos.right.parent = current_pos.left
                    current_pos.parent.left = current_pos.left

                    current_pos = current_pos.left

                elif current_pos.parent.right == current_pos:
                    # shift current_pos.right to current_pos
                    current_pos.right.parent = current_pos.parent
                    current_pos.left.parent = current_pos.right
                    current_pos.parent.right = current_pos.right

                    current_pos = current_pos.right

            return True

        return False
        

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