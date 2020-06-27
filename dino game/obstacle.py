import random

class Obstacle:
    size = 2.5
    height = size
    width = size
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def changeY(self, y):
        self.width = self.size
        n = random.randint(0,1)
        if (n == 1):
            self.width *= 2
            self.y -= y
