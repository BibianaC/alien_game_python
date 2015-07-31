from alien_game_python.player import Player

def test_init():
    player = Player()
    assert player.position == 0

def test_fire():
    player = Player()
    player.fire(90)
    assert player.impact_area == -6