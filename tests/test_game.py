from alien_game_python.player import Player
from alien_game_python.alien import Alien
from alien_game_python.game import Game

def test_init():
    player = Player()
    alien = Alien(5)
    game = Game(player, alien)
    assert game.player == player
    assert game.alien == alien