import random
from typing import List

import pygame
from CONSTANTS import *
from cherry import Cherry

class Game:
    def __init__(self):
        self.cherries = []
        self.board = [[None for i in range(NUM_COLS)] for j in range(NUM_ROWS)] 

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

        sX = CW * col
        sY = CH * row

        cherry = Cherry(sX, sY)

        self.board[row][col] = cherry 
        self.cherries.append(cherry)

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

        screen.fill((255, 255, 255))

        curr_time = pygame.time.get_ticks()

        if curr_time - prev_time >= SPAWN_CD:
            prev_time = curr_time        
            game.spawn_cherry()

        for cherry in game.cherries:
            cherry.draw(screen)

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
