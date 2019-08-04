import pygame
import os
from enemies.enemy import Enemy

class Scorpion(Enemy):
    imgs = [pygame.image.load(os.path.join("../game_assets/enemies/1", "1_run_" + '{:03x}'.format(x) + '.png')) for x in range(3)]
