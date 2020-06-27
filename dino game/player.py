import obstacle

class Player:
    jumpHeight = 0.5
    jumpCount = jumpHeight
    isJump = False
    width = 2.5
    height = 5
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def jump(self):
        self.isJump = True
