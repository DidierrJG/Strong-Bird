import pygame
from variables import WINDOW_WIDTH

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/images/environment/pipe.png")
        self.rect = self.image.get_rect()

        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - 153 // 2]
        else:
            self.image = pygame.transform.flip(self.image, False, False)
            self.rect.topleft = [x, y + 153 // 2]

    def update(self):
        self.rect.x -= 3

        if self.rect.right < 0:
            self.kill()