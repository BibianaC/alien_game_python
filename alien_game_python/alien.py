import random

class Alien(object):

    BOUNDS = range(-10, 10)
    MOVES = [-1, 1]

    def __init__(self, x_0):
        self.position = x_0

    def move(self, bounds=BOUNDS, moves=MOVES):        
        move_postion = self.position + random.choice(moves)
        if move_postion in bounds:
            self.position = move_postion