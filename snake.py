import pygame 
from CONSTANTS import *

class Snake(pygame.sprite.Sprite):
    def __init__(self, x: int, y:int, head:bool) -> None:
        super().__init__()
        self.mask = None 
        self.x = x
        self.y = y

        self.head = head
        self.next = None

        self.color = (255, 0, 0)

        self.image = pygame.Surface((W, H))
        self.image.fill(color=tuple(self.color))

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def draw(self, screen: pygame.surface.Surface) -> None:
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        screen.blit(self.image, self.rect)

    def move_up(self):
        self.y -= H
        if self.y < 0:
            self.y = SCREEN_HEIGHT - H

    def move_down(self):
        self.y += H
        if self.y > SCREEN_HEIGHT:
            self.y = 0
    
    def move_left(self):
        self.x -= W
        if self.x < 0:
            self.x = SCREEN_WIDTH - W

    def move_right(self):
        self.x += W
        if self.x > SCREEN_WIDTH:
            self.x = 0
            