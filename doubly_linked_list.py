""" Nodes of a doubly linked list also require a reference to the previous node """
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

""" Two-way linked list, unoptimised (most operations are still O(n)) """
class DoublyLinkedList:
    def __init__(self, root:Node = None):
        self.root = root

    """ Insert a new node before another """
    def add_before(self, item, data)->bool:
        start = self.root
        
        """ In case there is no root node or if the new node needs to be inserted before it """
        if start is None or start.data == item:
            new_node = Node(data)
            new_node.next = start
            start.prev = new_node
            self.root = new_node
            return True

        current_pos = start.next

        while current_pos is not None:
            if current_pos.data == item:
                new_node = Node(data)
                new_node.prev = current_pos.prev
                new_node.next = current_pos

                if current_pos.prev is not None:
                    current_pos.prev.next = new_node
                current_pos.prev = new_node

                return True

            current_pos = current_pos.next

        return False

    """ Insert a new node after another """
    def add_after(self, item, data)->bool:
        start = self.root
        current_pos = start

        while current_pos is not None:
            if current_pos.data == item:
                new_node = Node(data)
                new_node.prev = current_pos
                new_node.next = current_pos.next
                
                if current_pos.next is not None:
                    current_pos.next.prev = new_node
                current_pos.next = new_node

                return True

            current_pos = current_pos.next

        return False

    """ Delete a node """
    def delete(self, item)->bool:
        start = self.root

        if start is None:
            return False

        """ In case the node to be deleted is the first one """
        if start.data == item:
            if start.next is not None:
                start.next.prev = None
                self.root = start.next
            else:
                self.root = None
            return True

        current_pos = start.next

        while current_pos is not None:
            if current_pos.data == item:
                """
                Let's imagine this situation:
                   ... -> <- 1 -> <- (item) -> <- 2 -> ...

                This needs to turn into:
                    ... -> <- 1 -> <- 2 -> ...
                """
                if current_pos.next is not None:
                    current_pos.next.prev = current_pos.prev

                if current_pos.prev is not None:
                    current_pos.prev.next = current_pos.next

                return True

            current_pos = current_pos.next

        return False

    """ Print all values from the nodes in the list """
    def traverse(self):
        current_pos = self.root

        while current_pos is not None:
            print(current_pos.data)
            current_pos = current_pos.next

    """ Find a node by its value """
    def find(self, item)->Node:
        current_pos = self.root

        while current_pos is not None:
            if current_pos.data == item:
                return current_pos
            current_pos = current_pos.next

        return None

if __name__ == "__main__":
    dll = DoublyLinkedList(Node(3))

    """ 8 is inserted before 3, becomes the root of the list """
    dll.add_before(3, 8)

    """ 10 is inserted after 3 """
    dll.add_after(3, 10)

    """ 20 is inserted after 8 """
    dll.add_after(8, 20)

    print(f'Found 40? {dll.find(40) and dll.find(40).data}')

    print('All items:')

    """ 8, 20, 3, 10 """
    dll.traverse()
