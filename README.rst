# Spaceship vs Alien

## Introduction

There is a player with a spaceship at position 0 along an axis, and there is an alien at some unknown initial position x_0 on that axis. 

The player and the (computer-controlled) alien take turns.

The player tries to hit the alien. 

In each player turn the player can set the firing angle alpha of the spaceship and then fire it. 

The nozzle velocity v of the spaceship is fixed. 

The spaceship ball hits the ground at this distance x_impact from the spaceship: x_impact = (2cos(alpha)sin(alpha)v^2)/g where g = 9.81 m/s^2 is the earth's gravitational acceleration.

## Tests

Install test requirements::

  pip install -r test_requirements.txt


Run tests::

  py.test 

## How to play

- Before playing, install Python
- Open a terminal
- Run `$ python game_runner.rb`