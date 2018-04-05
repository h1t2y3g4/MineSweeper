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

        # 设置记录窗口参数
        self.record_window_size = (200, 50)
        self.record_window_color = (0, 0, 0)

        # 设置帧数
        self.fps = 60

        # 设置地雷数
        self.mine_number = 10

