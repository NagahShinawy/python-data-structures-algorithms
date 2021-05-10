"""
Python Data Structures - A Game-Based Approach
Queue class
Robin Andrews - https://compucademy.net/
"""

from collections import deque


class Queue:

    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        # if not self.is_empty():
        #     self.items.remove(self.items[0])
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self):
        return str(self.items)


if __name__ == '__main__':
    q = Queue()
    print(q)
    print(q.is_empty())
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    print(q)
    print(q.is_empty())
    print("dequeue", q.dequeue())
    print(q, q.is_empty())
    print("#" * 50)
    print(q.peek())  # return first item without removing it.
    print("Size:", q.size())

    # ##################  TASK  ######################
    print("*" * 100)
    qe = Queue()
    qe.enqueue("Learning")
    qe.enqueue("With")  # ["Learning", "With"]
    qe.dequeue()  # ["With"]
    qe.enqueue("Linked")  # ["With", "Linked"]
    qe.enqueue("In")   # ["With", "Linked", "In"]
    qe.dequeue()   # ["Linked", "In"]
    print(qe)
