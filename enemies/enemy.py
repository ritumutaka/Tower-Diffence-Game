import pygame
import math
import random


class Enemy:
    imgs = []

    def __init__(self):
        self.width = 64
        self.height = 64
        self.animation_count = 0
        self.health = 1
        self.vel = 3
        self.x = random.randint(-100, -self.width)
        self.y = random.randint(0, 700-self.height)
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
        self.x = self.x + 2

    def hit(self):
        """
        敵が死亡した場合にTrueを返し、healthを一つ削除する
        :return: Bool
        """
        self.health -= 1
        if self.health <= 0:
            return True
