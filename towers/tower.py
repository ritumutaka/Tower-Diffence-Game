import math
import pygame
import os


class Tower():
    """
    タワー用 親クラス
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.sell_price = [0, 0, 0]
        self.price = [0, 0, 0]
        self.level = 1
        self.selected = False
        self.menu = None
        self.tower_imgs = []

    def draw(self, win):
        """
        タワーを描画する
        :param win: surface
        :return: None
        """
        img = self.tower_imgs[self.level]
        win.blit(img, (self.x - img.get_width()/2, self.y - img.get_height()/2))

    def click(self, X, Y):
        """
        タワーがクリックされたかどうかを返す
        :param X: int
        :param Y: int
        :return: bool
        """
        if self.x <= X <= self.x + self.width:
            if self.y <= Y <= self.y + self.height:
                return True

        return False

    def sell(self):
        """
        タワーの売却処理
        :return: int
        """
        pass

    def upgrade(self):
        pass

    def move(self):
        pass


class Bullet():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.level = 1
        self.bullet_imgs = []

    def draw(self, win):
        """
        弾を描画する
        :param win: surface
        :return: None
        """
        img = self.bullet_imgs[self.level]
        win.blit(img, (self.x - img.get_width() / 2, self.y - img.get_height() / 2))

    def upgrade(self):
        pass


