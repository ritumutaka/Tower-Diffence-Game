import pygame
from .tower import Tower
import os

tower_imgs = []
for x in range(3):
    tower_imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("../game_assets/towers/archerTower", '{:03x}'.format(x) + '.png')), (120, 120)))

archer_imgs = []
for x in range(3):
    archer_imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("../game_assets/towers/archer", '{:03x}'.format(x) + '.png')), (120, 120)))


class ArcherTowerLong(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgs[:]
        self.archer_imgs = archer_imgs[:]
        self.archer_count = 1

    def draw(self, win):
        super().draw(win)
        if self.archer_count >= len(self.archer_imgs) * 3: # 3倍することで描画をゆっくりにする
            self.archer_count = 0

        archer = self.archer_imgs[self.archer_count // 3]
        win.blit(archer, ((self.x + self.width/2) - archer.get_width()/2, self.y - archer.get_height()))

        self.archer_count += 1

    def attack(self, enemies):
        """
        敵を攻撃する処理
        敵のリストを渡して、そのリストを処理
        :param enemies: list
        :return: None
        """
        pass
