import pygame


class TimeRecordWindow:
    def __init__(self, setting, field, screen):
        """时间记录窗口"""
        self.setting = setting
        self.screen = screen

        # 初始化窗口，并安放位置
        self.image = pygame.Surface(setting.record_window_size)
        self.image.fill(setting.record_window_color)
        self.rect = self.image.get_rect()
        self.rect.left = field.rect.left
        self.rect.y = 50

    def build_me(self):
        self.screen.blit(self.image, self.rect)


class NumberRecordWindow:
    def __init__(self, setting, field, screen):
        """剩余地雷数记录窗口"""
        self.setting = setting
        self.screen = screen

        # 初始化窗口，并安放位置
        self.image = pygame.Surface(setting.record_window_size)
        self.image.fill(setting.record_window_color)
        self.rect = self.image.get_rect()
        self.rect.right = field.rect.right
        self.rect.y = 50

    def build_me(self):
        self.screen.blit(self.image, self.rect)