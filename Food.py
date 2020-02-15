import random
import pygame


class Food:
    def __init__(self, boundary_x, boundary_y):
        self.boundary_x = boundary_x
        self.boundary_y = boundary_y
        self.generate_x = round(random.randrange(0, self.boundary_x-10) / 10.0) * 10
        self.generate_y = round(random.randrange(0, self.boundary_y-10) / 10.0) * 10

    def generate_food(self):
        self.generate_x = round(random.randrange(0, self.boundary_x-10) / 10.0) * 10
        self.generate_y = round(random.randrange(0, self.boundary_y-10) / 10.0) * 10

    def get_position(self):
        return self.generate_x, self.generate_y

    def draw(self, game_display, color):
        pygame.draw.rect(game_display, color, (self.generate_x, self.generate_y, 10, 10))
