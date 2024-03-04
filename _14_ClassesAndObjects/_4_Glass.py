class Glass:
    def __init__(self):
        self._content = 0
        self._capacity = 250

    def set_content(self, value):
        self._content = value

    def fill(self, ml):
        temp = self._content + ml
        if temp <= self._capacity:
            self.set_content(temp)
            return f"Glass filled with {ml} ml"
        return f"Cannot add {ml} ml"

    def empty(self):
        self.set_content(0)
        return "Glass is now empty"

    def info(self):
        space_left = self._capacity - self._content
        return f"{space_left} ml left"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())

