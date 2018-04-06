import pygame
from pygame.sprite import Sprite


class MineBlock(Sprite):

    def __init__(self, field, screen, setting):
        super().__init__()
        """初始化地雷方块，并确定绘制区域"""
        self.field = field
        self.screen = screen

        # 加载图片，并且设定第一个小方块的位置
        self.image = pygame.Surface(setting.mine_window_size)
        self.image.fill(setting.mine_block_color)
        self.rect = self.image.get_rect()
        self.rect.x = self.field.rect.left + 1
        self.rect.y = self.field.rect.top + 1

        # 算出小方块的尺寸，以及每行列所能容纳的小方块个数
        self.len = self.rect.width + 1
        self.high = self.rect.height + 1
        self.number_x = int(self.field.rect.width/self.len)
        self.number_y = int(self.field.rect.height/self.high)

<<<<<<< HEAD
        # 周围的地雷数
        self.count = 0

        # 各种检查条件
        self.left_clicked_flag = False  # 是否是被点开了的方块
        self.mine_flag = False  # 是否是地雷
        self.clicked_mine_flag = False  # 是否是点中的那个地雷
        self.banner_flag = False  # 是否是旗帜状态
        self.question_mark_flag = False  # 是否为问号状态
        self.first_click_flag = False  # 是否是第一次点击的方块
=======
        # 是否是被点开了的方块
        self.clicked_flag = False
>>>>>>> f144367de06850ba0bea4a4bea3922ffc08f2e23

    def built_me(self):
        # 将方块绘制到主屏幕
        self.screen.blit(self.image, self.rect)

<<<<<<< HEAD
=======
    def change_clicked_flag(self):
        # 改变翻开地雷的标志
        self.clicked_flag = True
>>>>>>> f144367de06850ba0bea4a4bea3922ffc08f2e23
