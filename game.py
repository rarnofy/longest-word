import string
import random
 
class Game:
    def __init__(self):
        self.grid = [] #initiation
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))