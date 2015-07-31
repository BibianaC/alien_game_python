from alien_game_python.player import Player

def test_init():
    player = Player()
    assert player.position == 0