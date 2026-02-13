import pygame
from variables import WINDOW_HEIGHT

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y, body):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for i in range(1, 4):
            self.image = pygame.image.load(f"assets/images/bird/muscle_bird_{i}.png")
            self.image = pygame.transform.scale(self.image, (34, 24))
            self.images.append(self.image)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.speed = 0
        self.clicked = False
        self.body = body

    def update(self, flying, game_over):
        if flying == True:
            self.speed += 0.5
            if self.speed > 8:
                self.speed = 8
            if self.rect.bottom < (WINDOW_HEIGHT - 102):
                self.rect.y += int(self.speed)

        if game_over == False:
            if self.body.in_exercise == True and self.clicked == False:
                self.speed = -10
                self.clicked = True
            if self.body.in_exercise == False:
                self.clicked = False

            self.counter += 1
            bird_cooldown = 10

            if self.counter > bird_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0

            self.image = self.images[self.index]

            self.image = pygame.transform.rotate(self.images[self.index], self.speed * -2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], self.speed * -90)