import pygame


class MineField:

    def __init__(self, screen_main, setting):
        """初始化扫雷区域，并确定其位置。"""
        self.screen = screen_main  # 获取主屏幕的属性
        self.setting = setting

        # 加载雷区图像并且获取图像和主界面的位置信息
        self.image = pygame.Surface(setting.minefield_window_size)
        self.image.fill(setting.minefield_color)
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 设置雷区位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 50

        # 设置胜利后字体
        self.font = pygame.font.SysFont("Calibri", self.setting.minefield_font_size)
        self.font2 = pygame.font.SysFont("华文仿宋", 30)
        self.font3 = pygame.font.SysFont("华文仿宋", 30)
        self.font2_picture = self.font2.render("按F5重新开始当前难度游戏", True, self.setting.minefield_font_color)
        self.font3_picture = self.font3.render("按Ctrl+F5重新开始游戏", True, self.setting.minefield_font_color)

    # 绘制雷区
    def build_me(self):
        self.screen.blit(self.image, self.rect)

    # 游戏胜利结束后绘制半透明蒙版
    def game_over_win(self):
        self.image = self.image.convert_alpha()
        self.image.fill(self.setting.game_over_color)

        # 把文字加上去
        self.font_picture = self.font.render("Victory!", True, self.setting.minefield_font_color)
        self.font_picture_rect = self.font_picture.get_rect()
        self.font_picture_rect.centerx = self.rect.centerx
        self.font_picture_rect.centery = self.rect.centery

        self.font2_picture_rect = self.font2_picture.get_rect()
        self.font2_picture_rect.centerx = self.rect.centerx
        self.font2_picture_rect.top = self.font_picture_rect.bottom + 20

        self.font3_picture_rect = self.font3_picture.get_rect()
        self.font3_picture_rect.centerx = self.rect.centerx
        self.font3_picture_rect.top = self.font2_picture_rect.bottom + 10

        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.font_picture, self.font_picture_rect)
        self.screen.blit(self.font2_picture, self.font2_picture_rect)
        self.screen.blit(self.font3_picture, self.font3_picture_rect)

    # 游戏失败结束后绘制半透明蒙版
    def game_over_fail(self):
        self.image = self.image.convert_alpha()
        self.image.fill(self.setting.game_over_color)

        # 把文字加上去
        self.font_picture = self.font.render("Defeat!", True, self.setting.minefield_font_color)
        self.font_picture_rect = self.font_picture.get_rect()
        self.font_picture_rect.centerx = self.rect.centerx
        self.font_picture_rect.centery = self.rect.centery

        self.font2_picture_rect = self.font2_picture.get_rect()
        self.font2_picture_rect.centerx = self.rect.centerx
        self.font2_picture_rect.top = self.font_picture_rect.bottom + 20

        self.font3_picture_rect = self.font3_picture.get_rect()
        self.font3_picture_rect.centerx = self.rect.centerx
        self.font3_picture_rect.top = self.font2_picture_rect.bottom + 10

        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.font_picture, self.font_picture_rect)
        self.screen.blit(self.font2_picture, self.font2_picture_rect)
        self.screen.blit(self.font3_picture, self.font3_picture_rect)
