import pygame 
from CONSTANTS import *

class Body(pygame.sprite.Sprite):
    def __init__(self, x: int, y:int, curr_dir : str = 'u') -> None:
        super().__init__()

        self.x = x
        self.y = y

        self.color = (255, 0, 0)

        self.image = pygame.Surface((W, H))
        self.image.fill(color=tuple(self.color))

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.x * W, self.y * H))

        self.curr_dir = curr_dir

    def move(self):
        if self.curr_dir == 'u':
            self.move_up()
        elif self.curr_dir == 'd':
            self.move_down()
        elif self.curr_dir == 'l':
            self.move_left()
        else:
            self.move_right()

    def draw(self, screen: pygame.surface.Surface) -> None:
        self.rect = self.image.get_rect(topleft=(self.x * W, self.y * H))
        screen.blit(self.image, self.rect)

    def move_up(self):
        self.y -= 1
        if self.y < 0:
            self.y = NUM_ROWS - 1

    def move_down(self):
        self.y += 1
        if self.y >= NUM_ROWS:
            self.y = 0
    
    def move_left(self):
        self.x -= 1
        if self.x < 0:
            self.x = NUM_COLS - 1

    def move_right(self):
        self.x += 1
        if self.x >= NUM_COLS:
            self.x = 0

class Snake(pygame.sprite.Sprite):
    def __init__(self, x: int, y:int) -> None:
        super().__init__()
        
        self.x = x 
        self.y = y

        self.full_body = [Body(x, y)]

    def draw(self, screen):
        for part in self.full_body:
            part.draw(screen)
    
    def update_body(self, board):
        for i in range(len(self.full_body) - 1):
            board[self.full_body[i].y][self.full_body[i].x] = None
            self.full_body[i].x = self.full_body[i + 1].x
            self.full_body[i].y = self.full_body[i + 1].y
            board[self.full_body[i].y][self.full_body[i].x] = 's'

    def move(self, board):
        self.update_body(board)
        self.full_body[-1].move()
        board[self.full_body[-1].y][self.full_body[-1].x] = 's'

    def update_dir(self, move_dir):
        self.full_body[-1].curr_dir = move_dir
