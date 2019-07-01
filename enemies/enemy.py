import pygame
import math

class Enemy:
    imgs = []
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.animation_count = 0
        self.health = 1
        self.vel = 3
        self.path = [(4, 382), (163, 383), (166, 178), (363, 180), (367, 446), (625, 450), (634, 321), (994, 315)]
        self.img = None
        self.path_pos = 0
        self.move_speed = 1

    def draw(self, win):
        """
        与えられた画像で敵を描画
        :param win: surface
        :return: None
        """
        self.animation_count += 1

        if self.animation_count >= len(self.imgs):
            self.animation_count = 0

        self.img = self.imgs[self.animation_count]
        win.blit(self.img, (self.x, self.y))
        self.move()

    def collide(self, X, Y):
        """
        受け取った座標に敵がいるかを返す
        :param x: int
        :param y: int
        :return: Bool
        """
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True

        return False

    def move(self):
        """
        敵の移動
        :return: None
        """
        x1, y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = self.path[-1][0] + 10, self.path[-1][1] + 0
        else:
            x2, y2 = self.path[self.path_pos+1]

        move_dirction = (x2 - x1) / (y2 - y1)
        self.x = (self.x + 1) * self.move_speed
        self.y = (self.x * move_dirction) * self.move_speed

        if x2 - self.move_speed / 2 <= self.x or self.x <= x2 + self.move_speed / 2 \
        and y2 - self.move_speed / 2 <= self.y or self.y <= y2 + self.move_speed / 2:
            self.path_pos += 1


    def hit(self):
        """
        敵が死亡した場合にTrueを返し、healthを一つ削除する
        :return: Bool
        """
        self.health -= 1
        if self.health <= 0:
            return True