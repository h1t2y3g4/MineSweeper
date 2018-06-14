class Setting:

    def __init__(self, difficulty, status):
        # 接受游戏记录数据
        self.difficulty = difficulty
        self.status = status

        if self.difficulty.display_info.current_w >= 1920 or self.difficulty.display_info.current_h >= 1080:
            if difficulty.easy:
                # 设置主界面的参数
                self.main_window_size = (600, 650)
                # 设置扫雷区域的参数。
                self.minefield_window_size = (501, 501)  # 20*20
                # 设置地雷数
                self.mine_number = 50
                # 游戏结束后在扫雷田上出现的文字尺寸
                self.minefield_font_size = 100
            elif difficulty.middle:
                # 设置主界面的参数
                self.main_window_size = (1000, 650)
                # 设置扫雷区域的参数。
                self.minefield_window_size = (901, 501)  # 36*20
                # 设置地雷数
                self.mine_number = 110
                # 游戏结束后在扫雷田上出现的文字尺寸
                self.minefield_font_size = 160
            elif difficulty.hard:
                # 设置主界面的参数
                self.main_window_size = (1300, 650)
                # 设置扫雷区域的参数。
                self.minefield_window_size = (1201, 501)  # 48*20
                # 设置地雷数
                self.mine_number = 200
                # 游戏结束后在扫雷田上出现的文字尺寸
                self.minefield_font_size = 200
            elif difficulty.very_hard:
                # 设置主界面的参数
                self.main_window_size = (1500, 800)
                # 设置扫雷区域的参数。
                self.minefield_window_size = (1401, 651)  # 56*26
                # 设置地雷数
                self.mine_number = 310
                # 游戏结束后在扫雷田上出现的文字尺寸
                self.minefield_font_size = 250
        else:
            if difficulty.easy:
                # 设置主界面的参数
                self.main_window_size = (600, 650)
                # 设置扫雷区域的参数。
                self.minefield_window_size = (501, 501)  # 20*20
                # 设置地雷数
                self.mine_number = 50
                # 游戏结束后在扫雷田上出现的文字尺寸
                self.minefield_font_size = 100
            elif difficulty.middle:
                # 设置主界面的参数
                self.main_window_size = (1000, 650)
                # 设置扫雷区域的参数。
                self.minefield_window_size = (901, 501)  # 36*20
                # 设置地雷数
                self.mine_number = 110
                # 游戏结束后在扫雷田上出现的文字尺寸
                self.minefield_font_size = 160
            elif difficulty.hard or difficulty.very_hard:
                # 设置主界面的参数
                self.main_window_size = (1300, 650)
                # 设置扫雷区域的参数。
                self.minefield_window_size = (1201, 501)  # 48*20
                # 设置地雷数
                self.mine_number = 200
                # 游戏结束后在扫雷田上出现的文字尺寸
                self.minefield_font_size = 200

        # 设置选择窗口相关属性
        self.chose_window_size = (400, 350)
        self.chose_font_color = (255, 0, 0)  # 设置选择难度按钮字体颜色

        # 设置主界面的参数
        self.background_color = (197, 234, 255)  # self.background_color = (145, 161, 187)
        self.icon = r"images/icon.png"

        # 设置扫雷区域的参数。
        self.minefield_color = (0, 0, 0)
        self.game_over_color = (255, 255, 255, 150)
        self.minefield_font_color = (0, 0, 0)  # 游戏结束后在扫雷田上出现的文字颜色

        # 初始化记录窗口的雷数
        self.status.fake_mine_number = self.mine_number

        # 设置地雷小方块的参数。
        self.mine_window_size = (24, 24)
        self.mine_block_color = (43, 87, 154)  # 未点开时的颜色
        self.mine_block_color_mousemotion = (101, 169, 241)  # 鼠标放在上面时的地雷颜色
        self.clicked_mine_block_color = (193, 204, 227)  # 翻开后的地雷方块颜色
        self.click_mine_block_picture = r"images/24乘24点击爆炸地雷.bmp"  # 点中地雷的那个方块的图片
        self.other_mine_block_picture = r"images/24乘24爆炸地雷.bmp"  # 除了点中的，其他地雷的图片
        self.right_click_banner_picture = r"images/24乘24旗帜.bmp"  # 右键第一次点击的小旗
        self.right_click_question_mark_picture = r"images/24乘24问号.bmp"  # 右键第二次点击问号
        self.bannered_mine_picture = r"images/24乘24旗帜地雷.bmp"  # 游戏结束后打开的被插上了旗帜的地雷

        # 设置数字
        self.picture_1 = r"images/24乘24的1.bmp"
        self.picture_2 = r"images/24乘24的2.bmp"
        self.picture_3 = r"images/24乘24的3.bmp"
        self.picture_4 = r"images/24乘24的4.bmp"
        self.picture_5 = r"images/24乘24的5.bmp"
        self.picture_6 = r"images/24乘24的6.bmp"
        self.picture_7 = r"images/24乘24的7.bmp"
        self.picture_8 = r"images/24乘24的8.bmp"

        # 设置记录窗口参数
        self.record_window_size = (200, 50)
        self.record_window_color = (197, 234, 255)
        self.font_color = (0, 0, 0)
        self.number_record_picture = r"images/50乘50地雷计数.bmp"
        self.time_record_picture = r"images/50乘50时钟.bmp"

        # 设置帧数
        self.fps = 60

