import pygame
from pygame.sprite import Sprite


class MineBlock(Sprite):

    def __init__(self, field, screen, setting, mousemotion_flage=False):
        super().__init__()
        """初始化地雷方块，并确定绘制区域"""
        self.field = field
        self.screen = screen
        self.mousemotion_flage = mousemotion_flage

        # 加载图片，并且设定第一个小方块的位置
        self.image = pygame.Surface(setting.mine_window_size)
        if self.mousemotion_flage:
            self.image.fill(setting.mine_block_color_mousemotion)
        else:
            self.image.fill(setting.mine_block_color)
        self.rect = self.image.get_rect()
        self.rect.x = self.field.rect.left + 1
        self.rect.y = self.field.rect.top + 1

        # 算出小方块的尺寸，以及没行列所能容纳的小方块个数
        self.len = self.rect.width + 1
        self.high = self.rect.height + 1
        self.number_x = int(self.field.rect.width/self.len)
        self.number_y = int(self.field.rect.height/self.high)

    def change_mousemotion_flage(self, boole=True):
        self.mousemotion_flage = boole
