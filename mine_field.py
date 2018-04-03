import pygame


class MineField:

    def __init__(self, screen_main, setting):
        """初始化扫雷区域，并确定其位置。"""
        self.screen = screen_main  # 获取主屏幕的属性

        # 加载雷区图像并且获取图像和主界面的位置信息
        self.image = pygame.Surface(setting.minefield_window_size)
        self.image.fill(setting.minefield_color)
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 设置雷区位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.y = 150

    # 绘制雷区
    def build_me(self):
        self.screen.blit(self.image, self.rect)
