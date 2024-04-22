

class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        if isinstance(element, str):
            self.data.append(element)
        else:
            raise ValueError("Only strings")

    def pop(self):
        if self.is_empty():
            raise IndexError("popping from empty stack")
        return self.data.pop()

    def top(self):
        if self.is_empty():
            return None
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0


    def __str__(self):
        # Format the stack elements from top to bottom
        return "[" + ", ".join(reversed(self.data)) + "]"
