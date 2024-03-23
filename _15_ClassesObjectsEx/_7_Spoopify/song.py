class Song:
    def __init__(self, name: str, length: float, single: bool):
        self.name = name
        self.length = length
        self.float = float
        self.single = single

    def get_info(self):
        return f"{self.name} - {self.length}"