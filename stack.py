class Stack:
    def __init__(self, size:int = 0):
        self.size = size
        self.data = []

    """ Adds a new item to the top of the stack (if not full) """    
    def push(self, item):
        if not self.is_full():
            self.data.append(item)

    """ Removes an item from the top of the stack """
    def pop(self):
        self.data.pop()

    """ Reads the item at the top of the stack """
    def peek(self):
        return self.data[-1]

    """ Determines whether the stack is empty """
    def is_empty(self):
        return len(self.data) <= 0

    """ Determines whether the stack is full """
    def is_full(self):
        return len(self.data) >= self.size

    """ Extra method that prints all items of the stack inline """
    def print_data(self):
        for i in range(0, len(self.data)):
            print(self.data[i], end="", flush=True)

"""
Exercise: using the Stack class, create a Python program that reverses the words of a string
"""

class Reverser:
    @staticmethod
    def reverse(string:str):
        s = Stack(len(string))

        for c in range(len(string) - 1, -1, -1):
            s.push(string[c])

        return s

sentence = "This sentence should be reversed"
r = Reverser.reverse(sentence)

r.print_data()