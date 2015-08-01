from alien_game_python.player import Player
from alien_game_python.alien import Alien
from alien_game_python.game import Game

import random

def player_turn(self, game, player):
    angle = raw_input("In what angle do you want to fire?").to_i
    impact_area = player.fire(angle)
    game.hit(impact_area)
    if game.over == False:
        print "You hit the ground! Try again" 


def run(self, game, player, alien):
    while game.over == False:
        self.alien if self.turn == self.player else self.player
        game.switch_turns
    print "Game over"

def start_game():
    bounds = range(-10, 10)
    player = Player()
    alien = Alien.new(random.choice(bounds))
    game = Game.new(player, alien)
    run(game, player, alien)

start_game