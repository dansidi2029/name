# def nameRecicnZER():
#     if NAME == "Sean":
#         print("hello to young to be 37")


import pygame
from stuff.player import Player
import Settings

pygame.init()

screen_dimeninstions= Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT
screen = pygame.display.set_mode(screen_dimeninstions)
pygame.display.set_caption("stuff")
# make a group of sprites so they aren't random and scattered
all_sprites = pygame.sprite.Group()
Dude = Player()
all_sprites.add(Dude)
clock = pygame.time.Clock()

running = True
while running:
    # check for user input events (keyboard, mouse, controller keys pressed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.K_w:
            # do something
            break

    # fill the screen window with a green color
    screen.fill((173,216,230))
    #Dude.update()
    all_sprites.draw(screen)
    # update the screen image
    pygame.display.flip()
    # update the game clock (60 fps)
    clock.tick(60)

# safelty close and quit the game window
pygame.quit()
