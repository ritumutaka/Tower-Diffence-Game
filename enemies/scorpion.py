import pygame
import os
from enemies.enemy import Enemy


class Scorpion(Enemy):
    imgs = []
    for x in range(3):
        imgs.append(pygame.transform.scale(
            pygame.image.load(os.path.join("../game_assets/enemies/1", '{:03x}'.format(x) + '.png')), (120, 120)))
