class Status:

    def __init__(self):
        """游戏状态记录"""
        self.game_going_flag = True  # 游戏是否继续
        self.first_click = True  # 是否为第一次点击鼠标左键
        self.game_win = False  # 游戏是否胜利
        self.game_begin_flag = False  # 是否进行了第一次点击，如果进行了那就开始计时
        self.F5_key = False  # 是否按下了F5

        self.easy = False  # 是否为简单模式
        self.middle = True  # 是否为一般模式
        self.hard = False  # 是否为困难模式

        self.first_click_time = 0  # 第一次点击的时刻，在函数中会初始化
        self.click_time = 0  # 当前点击时的时刻
        self.time_record = 0  # 在计数栏里面显示的已逝时间。在生成setting时会初始化

        self.fake_mine_number = 0  # 在计数栏里面显示的地雷数。在生成setting时会初始化

        self.difficulty_rect = []  # 选择难度时按钮rect的列表
        self.chose_flag = False  # 是否选择了难度
        self.ctrl_flag = False  # 是否按下了ctrl键
        self.alt_flag = False  # 是否按下了alt键




