import pygame
from variables import WINDOW_WIDTH, WINDOW_HEIGHT
import math
import random
from body_capture import BodyCapture
from bird import Bird
from pipe import Pipe
import cv2 as cv

pygame.init()

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Strong Bird")

#Draw text function
flappyBirdRegular = pygame.font.Font("assets/fonts/FlappyBirdRegular.ttf", 48)

def draw_text(text, font, text_color, x, y):
    image = font.render(text, True, text_color)
    window.blit(image, (x, y))

#Setup body_capture
body = BodyCapture()

#Load bird
bird_group = pygame.sprite.Group()
bird = Bird(100, WINDOW_HEIGHT // 2, body)
bird_group.add(bird)

#Pipe control
pipe_group = pygame.sprite.Group()
pipe_frequency = 4000
last_pipe = pygame.time.get_ticks() - pipe_frequency

#Load background
background_image = pygame.image.load("assets/images/environment/background.png")
background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

#Load ground
ground_image = pygame.image.load("assets/images/environment/ground.png")
ground_scroll = 0
    
#Frame rate control
clock = pygame.time.Clock()

#Game control
game_over = False
flying = False
pass_pipe = False
run = True
score = 0
elevations = 0

while run == True:
    clock.tick(30)

    #Draw background
    window.blit(background_image, (0, 0))

    #Draw bird
    bird_group.draw(window)
    bird_group.update(flying, game_over)

    #Draw pipes
    pipe_group.draw(window)

    #Draw ground
    window.blit(ground_image, (ground_scroll, WINDOW_HEIGHT - 102))

    #Check score
    if len(pipe_group) > 0:
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left \
        and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right \
        and pass_pipe == False:
            pass_pipe = True

        if pass_pipe == True:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                score += 1
                pass_pipe = False

    draw_text(str(score), flappyBirdRegular, (0, 0, 0), (WINDOW_WIDTH // 2), 30)

    #Collision control
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or bird.rect.top < 0:
        game_over = True

    #Check game
    if bird.rect.bottom >= (WINDOW_HEIGHT - 102):
        game_over = True
        flying = False

    #Loop ground
    if game_over == False and flying == True:
        #Pipe generation
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            #Load pipe
            pipe_height = random.randint(-100, 100)
            top_pipe = Pipe(WINDOW_WIDTH, 300 + pipe_height, 1)
            bottom_pipe = Pipe(WINDOW_WIDTH, 300 + pipe_height, 0)
            pipe_group.add(top_pipe)
            pipe_group.add(bottom_pipe)

            last_pipe = time_now

        ground_scroll -= 2
        if abs(ground_scroll) > 51:
            ground_scroll = 0

        pipe_group.update()


    #Check workout
    frame = body.update_detection()
    if frame is not None:
        cv.imshow("Body Capture", frame)

    if body.in_exercise == True and flying == False and game_over == False:
        flying = True
        elevations += 1

    draw_text("ELEVATIONS: " + str(elevations), flappyBirdRegular, (0, 0, 0), 0, (WINDOW_HEIGHT - 60))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            body.stop_detection()

    pygame.display.update()

pygame.quit()