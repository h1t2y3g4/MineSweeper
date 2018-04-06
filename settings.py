class Setting:

    def __init__(self):

        # 设置主界面的参数
        self.main_window_size = (600, 700)
        self.background_color = (197, 234, 255)  # self.background_color = (145, 161, 187)

        # 设置扫雷区域的参数。
        self.minefield_window_size = (501, 501)
        self.minefield_color = (0, 0, 0)

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
        self.record_window_color = (255, 255, 255)

        # 设置帧数
        self.fps = 60

        # 设置地雷数
        self.mine_number = 50

