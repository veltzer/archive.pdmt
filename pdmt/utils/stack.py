class Stack:
    def __init__(self):
        self.storage = list()

    def is_empty(self):
        return not self.storage

    def push(self, p):
        self.storage.append(p)

    def pop(self):
        return self.storage.pop()

    def yield_all(self):
        yield from self.storage
