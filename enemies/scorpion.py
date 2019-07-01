import pygame
import os

class Scorpiton:
    imgs = [pygame.image.load(os.path.join("game_assets/enemies/1", "1_run_" + '{:03x}'.format(x))) for x in range(3)]
