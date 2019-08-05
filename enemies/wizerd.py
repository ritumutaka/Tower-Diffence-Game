import pygame
import os
from enemies.enemy import Enemy


class Wizerd(Enemy):
    imgs = [pygame.image.load(os.path.join("../game_assets/enemies/2", '{:03x}'.format(x) + '.png')) for x in range(3)]
