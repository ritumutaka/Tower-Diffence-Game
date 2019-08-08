import pygame
from .tower import Tower
import os
import math

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
        self.range = 200
        self.inRange = False

    def draw(self, win):
        # rangeの円を描画
        circle_surface = pygame.Surface((self.range*2, self.range*2), pygame.SRCALPHA, 32)
        pygame.draw.circle(circle_surface, (0, 255, 0, 100), (self.range, self.range), self.range, 0)

        win.blit(circle_surface, (self.x - self.range, self.y - self.range))

        super().draw(win)
        if self.inRange:
            self.archer_count += 1
            if self.archer_count >= len(self.archer_imgs) * 3:  # 3倍することで描画をゆっくりにする
                self.archer_count = 0
        else:
            self.archer_count = 0

        archer = self.archer_imgs[self.archer_count // 3]
        win.blit(archer, ((self.x + self.width/2) - archer.get_width()/2, self.y - archer.get_height()))

    def change_range(self, r):
        """
        攻撃範囲を更新
        :param r: int
        :return: None
        """
        self.range = r

    def attack(self, enemies):
        """
        敵を攻撃する処理
        敵のリストを渡して、そのリストを処理
        :param enemies: list
        :return: None
        """
        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            x = enemy.x - self.width/2
            y = enemy.y - self.height/2

            dis = math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)
            if dis <= self.range:
                self.inRange = True
                enemy_closest.append(enemy)

