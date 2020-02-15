import pygame
from Snake import Snake
from Food import Food


pygame.init()

width, height = 500, 500
game_display = pygame.display.set_mode((width, height))

direction = 'east'
clock = pygame.time.Clock()
FPS = 10
end = False


def game_loop():
    global direction, end
    snake = Snake(300, 300, width, height)
    food = Food(width, height)

    while not end:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 'east':
                    direction = 'west'
                elif event.key == pygame.K_RIGHT and direction != 'west':
                    direction = 'east'
                elif event.key == pygame.K_UP and direction != 'south':
                    direction = 'north'
                elif event.key == pygame.K_DOWN and direction != 'north':
                    direction = 'south'

        snake.move(direction)

        if snake.check_boundary():
            end = True

        if snake.collide_self_check():
            end = True

        if snake.collide_food(food.get_position()[0], food.get_position()[1]):
            snake.increment_length(direction)
            food.generate_food()

        game_display.fill((255, 255, 255))
        snake.draw(game_display, (255, 0, 0))
        food.draw(game_display, (0, 255, 0))

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()


game_loop()
