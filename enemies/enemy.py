import pygame

class Enemy:
    imgs = []
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.animation_count = 0
        self.health = 1
        self.path = []
        self.img = None

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
        pass

    def hit(self):
        """
        敵が死亡した場合にTrueを返し、healthを一つ削除する
        :return: Bool
        """
        self.health -= 1
        if self.health <= 0:
            return True