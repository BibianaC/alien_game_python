import math

class Player(object):

    G = 9.81 # Gravitational acceleration
    V = 8 # Nozzle velocity v of the spaceship

    def __init__(self):
        self.position = 0

    def fire(self, angle, v=V, g=G ):
        self.impact_area = math.floor((2*math.cos(angle)*math.sin(angle)*v**2)/g)
