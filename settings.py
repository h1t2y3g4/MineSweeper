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
        self.mine_block_color = (43, 87, 154)
        self.mine_block_color_mousemotion = (101, 169, 241)  # 鼠标放在上面时的地雷颜色
        self.clicked_mine_block_color = (193, 204, 227)  # 翻开后的地雷方块颜色
        self.click_mine_block_picture = r"images/24乘24点击爆炸地雷.bmp"  # 点中地雷的那个方块的图片
        self.other_mine_block_picture = r"images/24乘24爆炸地雷.bmp"  # 除了点中的，其他地雷的图片

        # 设置记录窗口参数
        self.record_window_size = (200, 50)
        self.record_window_color = (0, 0, 0)

        # 设置帧数
        self.fps = 60

        # 设置地雷数
        self.mine_number = 100

