import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, image, window, body):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for i in range(1, 4):
            self.image = pygame.image.load(f"assets/images/buttons/reset_{i}.png")
            self.image = pygame.transform.scale(self.image, (150, 150))
            self.images.append(self.image)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.window = window
        self.clicked = False
        self.body = body

    def draw(self):
        self.counter += 1
        button_cooldown = 5

        if self.counter > button_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0

        self.image = self.images[self.index]
        
        action = False

        if self.body.in_exercise == True and self.clicked == False:
            action = True
            self.clicked = True
        if self.body.in_exercise == False:
            self.clicked = False

        self.window.blit(self.image, (self.rect.x, self.rect.y))

        return action