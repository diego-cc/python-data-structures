""" Each item in a linked list is a node that holds a value and a reference to the next node """
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """ Initialise a Singly Linked List with an optional root value """
    def __init__(self, root:Node = None):
        self.root = root

    """ Insert an item to the linked list before another """
    def add_before(self, item, data):
        start = self.root
        new_node = Node(data)

        """ If there is no root node or a new node needs to be inserted before it, make it the root node """
        if start is None or item == start.data:
            new_node.next = start
            self.root = new_node
            return True

        current_pos = start

        while current_pos.next is not None:
            if current_pos.next.data == item:
                new_node.next = current_pos.next
                current_pos.next = new_node
                return True

            current_pos = current_pos.next

        return False

    """ Insert an item to the linked list after anoter """
    def add_after(self, item, data):
        start = self.root
        new_node = Node(data)

        current_pos = start

        while current_pos is not None:
            if current_pos.data == item:
                new_node.next = current_pos.next
                current_pos.next = new_node
                break

            current_pos = current_pos.next

        if current_pos is None:
            return False
        return True

    """ Delete an item from the linked list """
    def delete(self, item):
        if self.root is None:
            return False

        current_pos = self.root

        if item == current_pos.data:
            self.root = current_pos.next
            return True

        while current_pos.next is not None:
            if current_pos.next.data == item:
                current_pos.next = current_pos.next.next
                return True

            current_pos = current_pos.next

        return False

    """ Display all items in the list """
    def traverse(self):
        current_pos = self.root

        while current_pos is not None:
            print(current_pos.data)
            current_pos = current_pos.next

    """ Find a node in the linked list """
    def find(self, item):
        current_pos = self.root

        while current_pos is not None:
            if current_pos.data == item:
                return current_pos

            current_pos = current_pos.next

        return None


if __name__ == "__main__":
    
    """ Initialise singly linked list without a root node """
    sll = SinglyLinkedList()

    """ 3 is not added, because there is no node with data = 2 in the list """
    sll.add_after(2, 3)

    """ 
    6 is added even though there is no node with data = 3 in the list,
    because the linked list was initialised without a root node 
    """
    sll.add_before(3, 6)

    """ 8 is added before 6 """
    sll.add_before(6, 8)

    """ Replace 8 with non-existing values and see the output """
    print(f'Found 8? {sll.find(8) and sll.find(8).data}')

    print('All values:')
    sll.traverse()