class Stack():

    def __init__(self):
        self.stack = []

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        temp = self.peek()
        self.stack.pop()
        return temp

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def is_empty(self):
        return True if len(self.stack) == 0 else False