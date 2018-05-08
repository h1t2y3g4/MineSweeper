from settings import Setting
from mine_field import MineField
from status import Status
from functions import *
from record_windows import *
from difficulty import *
import pygame


def main(difficulty):
    """
    整个程序是在游戏主循环之前创建好地雷等东西，然后在主循环中修改并更新，只创建了一次。
    :return:
    """

    # 初始化游戏状态记录类
    status = Status()

    # 初始化设置
    setting = Setting(difficulty, status)

    # 选择难度
    if difficulty.ctrl_F5_key:
        chose_difficulty(status, setting, difficulty)
        setting = Setting(difficulty, status)

    # 初始化程序界面
    screen_main = pygame.display.set_mode(setting.main_window_size)
    screen_main.fill(setting.background_color)
    ico = pygame.image.load(setting.icon).convert_alpha()
    pygame.display.set_icon(ico)
    pygame.display.set_caption('扫雷')

    # 初始化帧数
    fps = pygame.time.Clock()

    # 初始化扫雷区域
    field = MineField(screen_main, setting)
    field.build_me()

    # 初始化地雷小方块
    blocks = create_blocks(field, screen_main, setting)

    # 初始化记录窗口
    time_record_window = TimeRecordWindow(setting, field, screen_main, status)
    time_record_window.build_me()
    time_record_window.update_font()
    number_record_window = NumberRecordWindow(setting, field, screen_main, status)
    number_record_window.build_me()
    number_record_window.update_font()

    # 是否需要加上分辨率不足提示语
    if difficulty.display_info.current_w < 1920 and difficulty.display_info.current_h < 1080 and difficulty.very_hard:
        build_resolution_ratio_word(screen_main, time_record_window, setting)

    # 开始程序主循环
    while True:
        check_event(blocks, setting, status, difficulty)
        if status.F5_key:
            break

        update_blocks(blocks)
        game_over(field, status)
        update_record_windows(time_record_window, number_record_window, status)
        pygame.display.flip()
        fps.tick(setting.fps)
    return status


if __name__ == '__main__':
    difficulty = Difficulty()
    pygame.init()
    difficulty.display_info = pygame.display.Info()
    status = main(difficulty)
    while status.F5_key:
        status = main(difficulty)
