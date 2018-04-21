import pygame


class TimeRecordWindow:
    def __init__(self, setting, field, screen, status):
        """时间记录窗口"""
        self.setting = setting
        self.screen = screen
        self.field = field
        self.status = status

        # 初始化窗口，并安放位置
        self.image = pygame.Surface(setting.record_window_size)
        self.image.fill(setting.record_window_color)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.field.rect.left + int(self.field.rect.width * 0.2)
        self.rect.bottom = self.field.rect.top - 20

        # 把图片加上去
        self.picture = pygame.image.load(setting.time_record_picture)
        self.picture_rect = self.picture.get_rect()
        self.picture_rect.topleft = self.rect.topleft

        # 把文字加上去
        self.time_font = pygame.font.SysFont("Calibri", 40)
        self.time_font_picture = self.time_font.render("0", True, self.setting.font_color)
        self.time_font_picture_rect = self.time_font_picture.get_rect()
        self.time_font_picture_rect.midright = self.rect.midright

    def build_me(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.picture, self.picture_rect)

    def update_font(self):
        self.time_font_picture = self.time_font.render(str(self.status.time_record), True, self.setting.font_color)
        self.time_font_picture_rect = self.time_font_picture.get_rect()
        self.time_font_picture_rect.midright = self.rect.midright
        self.screen.blit(self.time_font_picture, self.time_font_picture_rect)


class NumberRecordWindow:
    def __init__(self, setting, field, screen, status):
        """剩余地雷数记录窗口"""
        self.setting = setting
        self.screen = screen
        self.field = field
        self.status = status

        # 初始化窗口，并安放位置
        self.image = pygame.Surface(setting.record_window_size)
        self.image.fill(setting.record_window_color)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.field.rect.left + int(self.field.rect.width * 0.8)
        self.rect.bottom = self.field.rect.top - 20

        # 把图片加上去
        self.picture = pygame.image.load(setting.number_record_picture)
        self.picture_rect = self.picture.get_rect()
        self.picture_rect.topleft = self.rect.topleft

        # 把文字加上去
        self.number_font = pygame.font.SysFont("Calibri", 40)
        self.number_font_picture = self.number_font.render(str(self.status.fake_mine_number), True, self.setting.font_color)
        """ 
        第一个参数是写的文字；
        第二个参数是个布尔值，这是否开启抗锯；
        第三个参数是字体的颜色；
        第四个是背景色，如果你想没有背景色（也就是透明），那么可以不加这第四个参数。
        """
        self.number_font_picture_rect = self.number_font_picture.get_rect()
        self.number_font_picture_rect.midright = self.rect.midright

    def build_me(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.picture, self.picture_rect)

    def update_font(self):
        self.number_font_picture = self.number_font.render(str(self.status.fake_mine_number), True,
                                                           self.setting.font_color)
        self.number_font_picture_rect = self.number_font_picture.get_rect()
        self.number_font_picture_rect.midright = self.rect.midright
        self.screen.blit(self.number_font_picture, self.number_font_picture_rect)
