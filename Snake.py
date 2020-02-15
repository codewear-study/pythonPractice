import pygame


class Snake:
    def __init__(self, head_x, head_y, boundary_x, boundary_y):
        self.head_x = head_x
        self.head_y = head_y
        self.length = 3
        self.body = [(head_x, head_y), (self.head_x - 10, self.head_y), (self.head_x - 20, self.head_y)]
        self.boundary_x = boundary_x
        self.boundary_y = boundary_y

    def get_head(self):
        return self.head_x, self.head_y

    def get_length(self):
        return self.length

    def move(self, direction):
        if direction == 'north':
            self.body = [(self.head_x, self.head_y - 10)] + self.body[:-1]
            self.head_y -= 10
        elif direction == 'south':
            self.body = [(self.head_x, self.head_y + 10)] + self.body[:-1]
            self.head_y += 10
        elif direction == 'west':
            self.body = [(self.head_x - 10, self.head_y)] + self.body[:-1]
            self.head_x -= 10
        elif direction == 'east':
            self.body = [(self.head_x + 10, self.head_y)] + self.body[:-1]
            self.head_x += 10

    def check_boundary(self):
        if (self.head_x % self.boundary_x) == 0 or (self.head_y % self.boundary_y) == 0:
            return True
        else:
            return False

    def increment_length(self, direction):
        if self.body[self.length - 2][0] - self.body[self.length - 1][0] != 0:
            if self.body[self.length - 2][0] - self.body[self.length - 1][0] > 0:
                self.body.append((self.body[self.length - 1][0] - 10, self.body[self.length - 1][1]))
            else:
                self.body.append((self.body[self.length - 1][0] + 10, self.body[self.length - 1][1]))
        else:
            if self.body[self.length - 2][1] - self.body[self.length - 1][1] > 0:
                self.body.append((self.body[self.length - 1][0], self.body[self.length - 1][1] - 10))
            else:
                self.body.append((self.body[self.length - 1][0], self.body[self.length - 1][1] + 10))
        self.length += 1

    def collide_self_check(self):
        head = (self.head_x, self.head_y)
        for part in self.body[1:]:
            if head == part:
                print('1')
                return True
        return False

    def collide_food(self, food_position_x, food_position_y):
        if self.get_head()[0] == food_position_x and self.get_head()[1] == food_position_y:
            return True
        else:
            return False

    def draw(self, game_display, color):
        for part in self.body:
            pygame.draw.rect(game_display, color, (part[0], part[1], 10, 10))
