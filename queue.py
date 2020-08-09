class Queue:
    """ Initialises a new queue with max_size """
    def __init__(self, max_size:int = 0):
        self.max_size = max_size
        self.data = []

    """ Adds a new item to the end of the queue (if not full) """
    def enqueue(self, item):
        if not self.is_full():
            self.data.append(item)

    """ Removes and returns an item from the front of the queue """
    def dequeue(self):
        if not self.is_empty():
            return self.data.pop(0)
        return None

    """ Returns item in front of the queue (if not empty) """
    def front(self):
        if not self.is_empty():
            return self.data[0]
        return None

    """ Determines whether the queue is empty """
    def is_empty(self):
        return len(self.data) <= 0

    """ Determines whether the queue is full """
    def is_full(self):
        return len(self.data) >= self.max_size

if __name__ == "__main__":

    """ Instantiate queue with max_size = 20 """
    q = Queue(20)

    """ Add 1, 2, 3, 4 to the queue """
    for i in range(1, 5):
        q.enqueue(i)

    """ Remove three items from the front of the queue """
    q.dequeue()
    q.dequeue()
    q.dequeue()

    """ Add 11, 12, 13, 14 to the end of the queue """
    for i in range(11, 15):
        q.enqueue(i)

    """ Remove and print all items from the queue """
    while q.front():
        print(q.dequeue())       