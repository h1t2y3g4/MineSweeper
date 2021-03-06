from mine_block import MineBlock
import sys
import pygame
import random
import time
import os


# 检查事件
def check_event(blocks, setting, status, difficulty):
    for event in pygame.event.get():
        # 点叉叉或者是按ESC退出游戏
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        # ctrl+F5重新开始游戏
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL):
            status.ctrl_flag = True
        elif event.type == pygame.KEYUP and (event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL):
            status.ctrl_flag = False
        elif event.type == pygame.KEYUP and event.key == pygame.K_F5:
            blocks.clear()
            status.game_going_flag = False
            status.F5_key = True
            if status.ctrl_flag:
                difficulty.ctrl_F5_key = True
            else:
                difficulty.ctrl_F5_key = False
            break
        # ctrl+w退出游戏
        elif status.ctrl_flag and (event.type == pygame.KEYUP and event.key == pygame.K_w):
            pygame.quit()
            sys.exit()
        # alt+F4退出游戏
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_LALT or event.key == pygame.K_RALT):
            status.alt_flag = True
        elif event.type == pygame.KEYUP and (event.key == pygame.K_LALT or event.key == pygame.K_RALT):
            status.alt_flag = False
        elif status.alt_flag and event.type == pygame.KEYUP and event.key == pygame.K_F4:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYUP and event.key == pygame.K_F10:
            os.system('charts.exe')  # 这样打开以后，相对文件目录还是在本文件开始算的，跟打开的文件没关系卧槽！

        else:
            if status.game_going_flag:  # 要游戏处于活跃状态才进行以下步骤
                response_if_win(blocks, status, difficulty)
                if event.type == pygame.MOUSEMOTION:
                    # 鼠标移动到方块上面该做的事
                    mouse_x, mouse_y = event.pos
                    response_mouse_position(mouse_x, mouse_y, blocks, setting)
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse_x, mouse_y = event.pos
                    button = event.button
                    if button == 1:
                        # 按下鼠标左键后该做的事
                        response_mouse_left_click(mouse_x, mouse_y, blocks, setting, status)
                    elif button == 3:
                        # 按下右键后该做的事
                        response_mouse_right_click(mouse_x, mouse_y, blocks, setting, status)
            else:  # 如果游戏不继续了，就翻开所有方块
                open_other_block(blocks, setting)


# 游戏胜利后，把成绩写入文件
def write_record_in_file(difficulty, status):
    difficult = "undefined"
    if difficulty.easy:
        difficult = 'easy'
    elif difficulty.middle:
        difficult = 'middle'
    elif difficulty.hard:
        difficult = 'hard'
    elif difficulty.very_hard:
        difficult = 'very_hard'
    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    used_time = status.time_record
    with open('charts/' + difficult + '.txt', 'a') as file_object:
        corrent = {'used_time': used_time, 'local_time': local_time}
        file_object.write(str(corrent) + '\n')
    with open('charts/difficult.txt', 'w') as f:
        f.write(difficult)


# 对游戏是否胜利做出响应
def response_if_win(blocks, status, difficulty):
    status.game_win = check_game_win_flag(blocks)
    if status.game_win:
        # 这里我需要把成绩记录到文件中
        status.game_going_flag = False

        write_record_in_file(difficulty, status)
        os.system('charts.exe')  # 这样打开以后，相对文件目录还是在本文件开始算的，跟打开的文件没关系卧槽！

        print("你赢了")


# 检查游戏是否胜利,返回status的记录旗帜。这里需要遍历一遍所有的地雷。
def check_game_win_flag(blocks):
    for block_y in blocks:
        for block in block_y:
            if not (block.left_clicked_flag or block.mine_flag):
                return False
    return True


# 当鼠标右键点击了方块时，作出反应。又是一遍遍历，同样可以多进程。
def response_mouse_right_click(mouse_x, mouse_y, blocks, setting, status):
    for block_y in blocks:
        for block in block_y:
            if block.rect.collidepoint(mouse_x, mouse_y):
                if not (block.left_clicked_flag or block.banner_flag or block.question_mark_flag):
                    # 如果是未点开，并且不是旗帜，并且不是问号
                    block.image = pygame.image.load(setting.right_click_banner_picture)
                    block.banner_flag = True
                    status.fake_mine_number -= 1
                elif block.banner_flag and not (block.left_clicked_flag or block.question_mark_flag):
                    # 如果是旗帜，并且未点开，并且不是问号
                    block.image = pygame.image.load(setting.right_click_question_mark_picture)
                    block.banner_flag = False
                    block.question_mark_flag = True
                    status.fake_mine_number += 1
                elif block.question_mark_flag and not (block.left_clicked_flag or block.banner_flag):
                    # 如果是问号，并且未点开，并且不是旗帜
                    block.image = pygame.Surface(setting.mine_window_size)
                    block.image.fill(setting.mine_block_color)
                    block.question_mark_flag = False


# 游戏结束以后，翻开其他的地雷小块。第五遍遍历了，可以多进程优化。
def open_other_block(blocks, setting):
    for block_y in blocks:
        for block in block_y:
            if block.mine_flag and not block.clicked_mine_flag:
                if not block.banner_flag:
                    block.image = pygame.image.load(setting.other_mine_block_picture)
                elif block.banner_flag:
                    block.image = pygame.image.load(setting.bannered_mine_picture)


# 当鼠标左键点击了没有翻开的地雷的时候，做出反应。一遍遍历，可多进程。
def response_mouse_left_click(mouse_x, mouse_y, blocks, setting, status):
    for block_y in blocks:
        for block in block_y:
            # 双层循环内的判断
            if not block.left_clicked_flag:
                # 如果当前方块是没有左键点过的
                if block.rect.collidepoint(mouse_x, mouse_y):
                    if not block.banner_flag:
                        # 如果不是旗子，可以是问号
                        block.left_clicked_flag = True
                        if status.first_click:
                            # 检测之前是否点了第一下，如果之前没有点，那么这个方块就作为第一次点击的方块，打上记号
                            block.first_click_flag = True
                            status.first_click_time = time.time()
                            status.game_begin_flag = True
                        if block.mine_flag:
                            # 如果点开的这个方块是地雷，则加载点开爆炸地雷图片
                            block.image = pygame.image.load(setting.click_mine_block_picture)
                            block.built_me()
                            block.clicked_mine_flag = True
                            status.game_going_flag = False
                        else:
                            # 如果点开的这个方块不是地雷,根据count的数值来加载图片
                            if block.count == 0:
                                block.image.fill(setting.clicked_mine_block_color)
                                x = block_y.index(block)
                                y = blocks.index(block_y)
                                if status.first_click:
                                    # 第一次点击以后再生成地雷
                                    create_mines(blocks, setting)
                                    status.first_click = False
                                # 找出连续的count为0的方块
                                automatic_click_consecutive_block(x, y, blocks, setting)
                            else:
                                block.image = pygame.image.load("images/24乘24的" + str(block.count) + ".bmp")


# 找出连续的count为0的方块
def automatic_click_consecutive_block(x, y, blocks, setting):
    for der_y in (-1, 0, 1):
        for der_x in (-1, 0, 1):
            try:
                if y + der_y < 0 or x + der_x < 0 or y + der_y > blocks[0][0].number_y or x + der_x > blocks[0][0].number_x:
                    continue
                if not blocks[y + der_y][x + der_x].left_clicked_flag:
                    blocks[y + der_y][x + der_x].left_clicked_flag = True
                    if blocks[y + der_y][x + der_x].count == 0:
                        blocks[y + der_y][x + der_x].image.fill(setting.clicked_mine_block_color)
                        automatic_click_consecutive_block(x + der_x, y + der_y, blocks, setting)
                    else:
                        blocks[y + der_y][x + der_x].image = pygame.image.load("images/24乘24的" + str(blocks[y + der_y][x + der_x].count) + ".bmp")
            except IndexError:
                continue


# 当鼠标移动到没有翻开的方块上时作出反应。这里需要遍历一遍地雷列表，这个可以多进程化。
def response_mouse_position(mouse_x, mouse_y, blocks, setting):
    for block_y in blocks:
        for block in block_y:
            if not block.left_clicked_flag:  # 如果当前方块是没有左键点过的
                if block.rect.collidepoint(mouse_x, mouse_y):  # 这是一个pygame内置函数，检测给的坐标点时候在当前surface对象内部
                    if not (block.banner_flag or block.question_mark_flag):
                        block.image.fill(setting.mine_block_color_mousemotion)
                elif block.banner_flag:
                    block.image = pygame.image.load(setting.right_click_banner_picture)
                elif block.question_mark_flag:
                    block.image = pygame.image.load(setting.right_click_question_mark_picture)
                else:
                    block.image.fill(setting.mine_block_color)


# 创建地雷列表
def create_blocks(field, screen_main, setting):
    blocks = []
    block = MineBlock(field, screen_main, setting)
    """
        双层循环填满地雷列表，注意用的是公式。也就是说每次都要创建一个新的地雷实例，然后通过算法直接修改坐标值，每个坐标属性
    只修改了一次。然后add了一次这个实例就废了，下一轮循环就又创建了一个地雷实例。
        为什么不只创建一次实例，然后通过while循环累加两个坐标值，每循环一次就add一次到编组中呢？这关系到python动态语言的性质，
    放到这个例子中来大概就是说，不能通过实例对象调用+=这种自身的运算来给类属性赋值，但可以通过类对象来进行这种运算赋值。哎呀
    绕晕了，查到的资料也没怎么看懂。http://python.jobbole.com/85100/
        blocks[y][x]。这样的坐标表示就是先处理行，再处理列，这样更符合习惯一点。
    """
    for block_number_y in range(block.number_y):
        blocks.append([])
        for block_number_x in range(block.number_x):
            block = MineBlock(field, screen_main, setting)
            block.rect.x = block.field.rect.left + 1 + block_number_x * block.len
            block.rect.y = block.field.rect.top + 1 + block_number_y * block.high
            blocks[block_number_y].append(block)
    return blocks


# 在小方块中生成地雷和周围方块的雷数
def create_mines(blocks, setting):
    mine_count = 0
    number_x = blocks[0][0].number_x
    number_y = blocks[0][0].number_y
    while mine_count < setting.mine_number:
        rand_x = random.randint(0, number_x - 1)
        rand_y = random.randint(0, number_y - 1)
        if check_first_clicked_block(blocks, rand_x, rand_y) and not (blocks[rand_y][rand_x].left_clicked_flag or blocks[rand_y][rand_x].mine_flag):
            blocks[rand_y][rand_x].mine_flag = True
            mine_count += 1
            # 将此雷块周围雷块的count属性+1
            for der_y in (-1, 0, 1):
                for der_x in (-1, 0, 1):
                    try:
                        if rand_y + der_y < 0 or rand_x + der_x < 0 or rand_y + der_y > blocks[0][0].number_y or rand_x + der_x > blocks[0][0].number_x:
                            continue
                        blocks[rand_y + der_y][rand_x + der_x].count += 1
                    except IndexError:
                        continue


# 检查现在想要生成的地雷的这个方块，周围八个格子里面有没有第一个点击的方块
def check_first_clicked_block(blocks, rand_x, rand_y):
    for der_y in (-1, 0, 1):
        for der_x in (-1, 0, 1):
            try:
                if blocks[rand_y + der_y][rand_x + der_x].first_click_flag:
                    return False
            except IndexError:
                continue
    return True


# 将地雷列表绘制到主屏幕上面去。第六遍遍历，貌似也可以多进程。
def update_blocks(blocks):
    for block_y in blocks:
        for block in block_y:
            block.built_me()


# 更新记录窗口显示的时间
def update_record_windows(time_record_window, number_record_window, status):
    if status.game_begin_flag and status.game_going_flag:
        # 更新时间显示
        status.click_time = time.time()
        status.time_record = int(status.click_time - status.first_click_time)
        time_record_window.build_me()
        time_record_window.update_font()

        # 更新地雷显示
        number_record_window.build_me()
        number_record_window.update_font()


def build_resolution_ratio_word(screen, time_record_window, setting):
    # 获得窗口rect信息
    screen_rect = screen.get_rect()

    text = pygame.font.SysFont("华文仿宋", 28)
    text_picture = text.render("当前屏幕分辨率不足，回到困难模式", True, setting.font_color)
    text_picture_rect = text_picture.get_rect()
    text_picture_rect.centerx = screen_rect.centerx
    text_picture_rect.centery = time_record_window.rect.centery
    screen.blit(text_picture, text_picture_rect)


# 游戏结束后绘制半透明蒙版
def game_over(field, status):
    if not status.game_going_flag:
        if status.game_win:
            field.game_over_win()
        else:
            field.game_over_fail()


# 游戏开始之前创建选择难度窗口并选择
def chose_difficulty(status, setting, difficulty):
    # 初始化窗口
    screen_chose = pygame.display.set_mode(setting.chose_window_size)
    screen_chose.fill(setting.background_color)
    ico = pygame.image.load(setting.icon).convert_alpha()
    pygame.display.set_icon(ico)
    pygame.display.set_caption("扫雷")

    # 显示文字
    set_font(screen_chose, setting, status)

    fps = pygame.time.Clock()

    # 开始检测点击位置循环
    while True:
        check_chose(status, difficulty)
        pygame.display.flip()
        if status.chose_flag:
            break
        fps.tick(setting.fps)


# 检查选择的是什么难度
def check_chose(status, difficulty):
    for event in pygame.event.get():
        # 点叉叉或者是按ESC退出游戏
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        # ctrl+w退出游戏
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL):
            status.ctrl_flag = True
        elif event.type == pygame.KEYUP and (event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL):
            status.ctrl_flag = False
        elif status.ctrl_flag and (event.type == pygame.KEYUP and event.key == pygame.K_w):
            pygame.quit()
            sys.exit()
        # alt+F4退出游戏
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_LALT or event.key == pygame.K_RALT):
            status.alt_flag = True
        elif event.type == pygame.KEYUP and (event.key == pygame.K_LALT or event.key == pygame.K_RALT):
            status.alt_flag = False
        elif status.alt_flag and event.type == pygame.KEYUP and event.key == pygame.K_F4:
            pygame.quit()
            sys.exit()
        else:
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos
                button = event.button
                if button == 1:
                    i = 0
                    for rect in status.difficulty_rect:
                        if rect.collidepoint(mouse_x, mouse_y):
                            if i == 0:
                                difficulty.easy = True
                                difficulty.middle = False
                                difficulty.hard = False
                                difficulty.very_hard = False
                            elif i == 1:
                                difficulty.easy = False
                                difficulty.middle = True
                                difficulty.hard = False
                                difficulty.very_hard = False
                            elif i == 2:
                                difficulty.easy = False
                                difficulty.middle = False
                                difficulty.hard = True
                                difficulty.very_hard = False
                            elif i == 3:
                                difficulty.easy = False
                                difficulty.middle = False
                                difficulty.hard = False
                                difficulty.very_hard = True
                            status.chose_flag = True
                            if i == 4:
                                os.system('charts.exe')
                                status.chose_flag = False
                        i += 1


# 设置选择难度窗口描述文本
def set_font(screen, setting, status):

    # 获得窗口rect信息
    screen_rect = screen.get_rect()

    font_build("请选择难度", (screen_rect.centerx, screen_rect.y + 20), 30, screen, setting.font_color)
    font_build("(直接点击）", (screen_rect.centerx, screen_rect.y + 60), 20, screen, setting.font_color)
    rect = font_build("简单", (screen_rect.centerx - 100, screen_rect.y + 100), 30, screen, setting.chose_font_color, True)
    status.difficulty_rect.append(rect)
    rect = font_build("中等", (screen_rect.centerx, screen_rect.y + 100), 30, screen, setting.chose_font_color, True)
    status.difficulty_rect.append(rect)
    rect = font_build("困难", (screen_rect.centerx + 100, screen_rect.y + 100), 30, screen, setting.chose_font_color, True)
    status.difficulty_rect.append(rect)
    rect = font_build("非常困难(仅支持1080P屏幕)", (screen_rect.centerx, screen_rect.y + 145), 25, screen, setting.chose_font_color,
                      True)
    status.difficulty_rect.append(rect)
    font_build("任何时候按F5重新开始当前难度游戏", (screen_rect.centerx, screen_rect.y + 190), 20, screen, setting.font_color)
    font_build("任何时候按ctrl+F5重新开始游戏", (screen_rect.centerx, screen_rect.y + 230), 20, screen, setting.font_color)
    rect = font_build("查看排行榜", (screen_rect.centerx, screen_rect.y + 270), 30, screen, setting.chose_font_color, True)
    status.difficulty_rect.append(rect)
    font_build("copyright © 陈守阳", (screen_rect.centerx, screen_rect.y + 320), 18, screen, setting.font_color)


def font_build(content, pos, font_size, screen, color, bold=False):
    # 显示“请选择难度”
    text = pygame.font.SysFont("华文仿宋", font_size)
    text.set_bold(bold)
    text_picture = text.render(content, True, color)
    text_picture_rect = text_picture.get_rect()
    text_picture_rect.centerx = pos[0]
    text_picture_rect.y = pos[1]
    screen.blit(text_picture, text_picture_rect)
    return text_picture_rect
