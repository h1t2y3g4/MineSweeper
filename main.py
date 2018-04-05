from settings import Setting
from mine_field import MineField
from status import Status
from functions import *
from record_windows import *
import pygame


def main():
    """
    整个程序是在游戏主循环之前创建好地雷等东西，然后在主循环中修改并更新，只创建了一次。
    :return:
    """
    # 初始化程序界面
    setting = Setting()
    pygame.init()
    screen_main = pygame.display.set_mode(setting.main_window_size)
    screen_main.fill(setting.background_color)
    pygame.display.set_caption('扫雷')

    # 初始化帧数
    fps = pygame.time.Clock()

    # 初始化游戏状态记录类
    status = Status()

    # 初始化扫雷区域
    field = MineField(screen_main, setting)
    field.build_me()

    # 初始化地雷小方块
    blocks = create_blocks(field, screen_main, setting)

    # 初始化记录窗口
    time_record_window = TimeRecordWindow(setting, field, screen_main)
    time_record_window.build_me()
    number_record_window = NumberRecordWindow(setting, field, screen_main)
    number_record_window.build_me()

    # 开始程序主循环
    while True:
        check_event(blocks, setting, status)
        update_blocks(blocks)
        pygame.display.flip()
        fps.tick(setting.fps)


if __name__ == '__main__':
    main()
