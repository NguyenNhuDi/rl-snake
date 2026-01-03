import random
from typing import List

import pygame
from CONSTANTS import *
from cherry import Cherry
from snake import Snake

class Game:
    def __init__(self):
        self.cherries = []
        self.board = [[None for i in range(NUM_COLS)] for j in range(NUM_ROWS)] 
        self.snake = Snake(
            (NUM_COLS // 2) * W, 
            (NUM_ROWS // 2) * H, head=True
        )

        self.move_snake = self.snake.move_up

    def is_full(self):
        for row in self.board:
            for item in row:
                if item is None:
                    return False
                
        return True

    def spawn_cherry(self):
        if self.is_full():
            return
        
        col = random.randint(0, NUM_ROWS - 1)
        row = random.randint(0, NUM_ROWS - 1)

        while self.board[row][col] is not None:
            col = random.randint(0, NUM_ROWS - 1)
            row = random.randint(0, NUM_ROWS - 1)

        sX = W * col
        sY = H * row

        cherry = Cherry(sX, sY)

        self.board[row][col] = cherry 
        self.cherries.append(cherry)

    def draw_game(self, screen):
        for cherry in self.cherries:
            cherry.draw(screen)

        self.snake.draw(screen)

def main():
    game = Game()

    game.spawn_cherry()
    game.spawn_cherry()

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(f'Snake')

    gameOn = True
    start_time = pygame.time.get_ticks()
    prev_time = start_time
    while gameOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOn = False


        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_q]:
            gameOn = False

        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            game.move_snake = game.snake.move_left
        elif pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
            game.move_snake = game.snake.move_up
        elif pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            game.move_snake = game.snake.move_right
        elif pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]:
            game.move_snake = game.snake.move_down

        screen.fill((255, 255, 255))

        curr_time = pygame.time.get_ticks()

        if curr_time - prev_time >= MOVE_CD:
            prev_time = curr_time        
            game.move_snake()

        if curr_time - prev_time >= 500:
            prev_time = curr_time        
            game.snake.move_up()

        game.draw_game(screen)

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
