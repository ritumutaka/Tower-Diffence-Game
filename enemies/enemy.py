import pygame
import math


class Enemy:
    imgs = []

    def __init__(self):
        self.width = 64
        self.height = 64
        self.animation_count = 0
        self.health = 1
        self.vel = 3
        self.path = [(4, 382), (163, 383), (166, 178), (363, 180), (367, 446), (625, 450), (634, 321), (994, 315)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
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
        :param X: int
        :param Y: int
        :return: Bool
        """
        if self.x <= X <= self.x + self.width:
            if self.y <= Y <= self.y + self.height:
                return True

        return False

    def move(self):
        """
        敵の移動
        :return: None
        """
        if self.path_pos + 1 >= len(self.path):
            x1, y1 = self.path[-2][0], self.path[-2][1]
            x2, y2 = self.path[-1][0] + 10, self.path[-1][1] + 0
        else:
            x1, y1 = self.path[self.path_pos]
            x2, y2 = self.path[self.path_pos + 1]

        # TODO: 敵の移動

        # self.x = self.x + self.move_speed * move_direction_x
        # self.y = self.y + self.move_speed * move_direction_y

        if (x2 - self.x) ** 2 < self.move_speed and (y2 - self.y) ** 2 < self.move_speed:
            self.path_pos += 1

    def hit(self):
        """
        敵が死亡した場合にTrueを返し、healthを一つ削除する
        :return: Bool
        """
        self.health -= 1
        if self.health <= 0:
            return True
