from alien_game_python.alien import Alien

def test_init():
    alien = Alien(5)
    assert alien.position == 5

def test_move():
    alien1 = Alien(5)
    alien2 = Alien(10)
    alien3 = Alien(-10)
    alien1.move()
    alien2.move()
    alien3.move()
    assert alien1.position == 4 or alien1.position == 6
    assert alien2.position == 9
    assert alien3.position == -9