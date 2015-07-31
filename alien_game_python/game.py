class Game(object):

    def __init__(self, player, alien):
        self.player = player
        self.alien = alien
        self.turn = player

    def switch_turns(self):
        self.turn = (self.alien if self.turn == self.player else self.player)

    def hit(self, impact_area):
        self.over = (impact_area == self.alien.position)