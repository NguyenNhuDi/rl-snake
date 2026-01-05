import random
from typing import List

import pygame
from CONSTANTS import *
from cherry import Cherry
from snake import Snake, Body

class Game:
    def __init__(self):
        self.cherries = []
        self.snake = Snake(
            NUM_COLS // 2, 
            NUM_ROWS // 2
        )
        self.board = [[None for i in range(NUM_COLS)] for j in range(NUM_ROWS)] 
        self.board[NUM_ROWS // 2][NUM_COLS // 2] = 'sh'

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

        cherry = Cherry(col, row)

        self.board[row][col] = cherry 
        self.cherries.append(cherry)

    def eat_cherry(self):
        next_x = self.snake.full_body[-1].x
        next_y = self.snake.full_body[-1].y

        curr_dir = self.snake.full_body[-1].curr_dir

        if curr_dir == 'u':
            next_y -= 1

            if next_y < 0:
                next_y = NUM_ROWS - 1
        elif curr_dir == 'd':
            next_y += 1

            if next_y >= NUM_ROWS:
                next_y = 0
        elif curr_dir == 'l':
            next_x -= 1

            if next_x < 0:
                next_x = NUM_COLS - 1
        else:
            next_x += 1
            if next_x >= NUM_COLS:
                next_x = 0

        found = False 
        cherry_ate = -1
        for i, cherry in enumerate(self.cherries):
            if cherry.x == next_x and \
               cherry.y == next_y:
                self.snake.full_body.append(Body(cherry.x, cherry.y, curr_dir))
                cherry_ate = i
                found = True
                break 

        if found:
            self.cherries.pop(cherry_ate)

            self.spawn_cherry()
            return True
            
        return False
 

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
            game.snake.update_dir('l')
        elif pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
            game.snake.update_dir('u')
        elif pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            game.snake.update_dir('r')
        elif pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]:
            game.snake.update_dir('d')

        screen.fill((255, 255, 255))

        curr_time = pygame.time.get_ticks()

        if curr_time - prev_time >= MOVE_CD:
            prev_time = curr_time        
            if not game.eat_cherry():
                game.snake.move(game.board)

        game.draw_game(screen)



        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
