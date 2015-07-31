from alien_game_python.alien import Alien

def test_init():
    alien = Alien(5)
    assert alien.position == 5