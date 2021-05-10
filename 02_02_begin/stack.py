"""
Python Data Structures - A Game-Based Approach
Stack class
Robin Andrews - https://compucademy.net/
"""


class Stack:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    @property
    def is_empty(self):
        # return len(self.items) == 0
        # return not self.items
        return True if not self.items else False

    def push(self, item):
        self.items.append(item)

    def pop(self):
        # removed_item = self.items[-1:][0]
        # self.items = self.items[:-1]
        # return removed_item
        return self.items.pop()  # remove the last item from the list

    def peek(self):
        return self.items[-1]

    @property
    def size(self):
        return len(self.items)

    def __repr__(self):
        return str(self.items)


def main():
    stack = Stack()
    print(stack, stack.is_empty, stack.size)
    items = [9, 50, 34]
    stack.push(45)
    stack.push(12)
    stack.push(10)
    stack.push(8)
    # print(stack)
    print("#" * 50)
    for itm in items:
        stack.push(itm)
    print("Len", len(stack))
    print("pop", stack.pop())
    print("Len", len(stack))

    print("#" * 100)

    for itm in stack:
        print(itm)

    print(stack)
    print(stack.peek())
    print(stack.is_empty)


if __name__ == "__main__":
    main()
