import random

class stimulus:
    def __init__(self):
        self.row = random.randint(0, 2)
        self.col = random.randint(0, 2)
    def Position(self):
        return(self.row, self.col)
    