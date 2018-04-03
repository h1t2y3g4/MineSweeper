from pygame.sprite import Sprite
import pygame


class MouseMove(Sprite):

    def __init__(self, mouse_x, mouse_y):  # 这里需要传递field
        super().__init__()
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y

        # 初始化鼠标点
        self.image = pygame.Surface((1, 1))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = self.mouse_x
        self.rect.y = self.mouse_y
