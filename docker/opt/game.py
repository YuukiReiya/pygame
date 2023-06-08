import pygame

class Game():

    cnt = 0

    def __init__(self):
        print("Game::__init__")

    def update(self):
        print(f"Game::update:{self.cnt}")
        self.cnt = self.cnt+1

    def draw(self):
        print("Game::draw")

    