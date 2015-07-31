from alien_game_python.player import Player
from alien_game_python.alien import Alien
from alien_game_python.game import Game

def test_init():
    player = Player()
    alien = Alien(5)
    game = Game(player, alien)
    assert game.player == player
    assert game.alien == alien

def test_switch_turns():
    player = Player()
    alien = Alien(5)
    game = Game(player, alien)
    assert game.turn == player
    game.switch_turns()
    assert game.turn == alien
    assert game.turn != player
    game.switch_turns()
    assert game.turn == player