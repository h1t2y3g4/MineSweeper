from mine_block import MineBlock
import sys
import pygame
import random
import os


# 检查事件
def check_event(blocks, setting, status):
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYUP and event.key == pygame.K_F5:
            """
            python = sys.executable
            os.execl(python, python, *sys.argv)
            """
            blocks.clear()
            status.game_going_flag = False
            break
        else:
            if status.game_going_flag:
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
                        response_mouse_right_click(mouse_x, mouse_y, blocks, setting)
            else:
                open_other_block(blocks, setting)


# 当鼠标右键点击了方块时，作出反应
def response_mouse_right_click(mouse_x, mouse_y, blocks, setting):
    for block_y in blocks:
        for block in block_y:
            if block.rect.top <= mouse_y <= block.rect.bottom and block.rect.left <= mouse_x <= block.rect.right:
                if not (block.left_clicked_flag or block.banner_flag or block.question_mark_flag):
                    # 如果是未点开，并且不是旗帜，并且不是问号
                    block.image = pygame.image.load(setting.right_click_banner_picture)
                    block.banner_flag = True
                elif block.banner_flag and not (block.left_clicked_flag or block.question_mark_flag):
                    # 如果是旗帜，并且未点开，并且不是问号
                    block.image = pygame.image.load(setting.right_click_question_mark_picture)
                    block.banner_flag = False
                    block.question_mark_flag = True
                elif block.question_mark_flag and not (block.left_clicked_flag or block.banner_flag):
                    # 如果是问号，并且未点开，并且不是旗帜
                    block.image = pygame.Surface(setting.mine_window_size)
                    block.image.fill(setting.mine_block_color)
                    block.question_mark_flag = False


# 游戏结束以后，翻开其他的地雷小块
def open_other_block(blocks, setting):
    for block_y in blocks:
        for block in block_y:
            if block.mine_flag and not block.clicked_mine_flag:
                if not block.banner_flag:
                    block.image = pygame.image.load(setting.other_mine_block_picture)
                elif block.banner_flag:
                    block.image = pygame.image.load(setting.bannered_mine_picture)


# 当鼠标左键点击了没有翻开的地雷的时候，做出反应
def response_mouse_left_click(mouse_x, mouse_y, blocks, setting, status):
    for block_y in blocks:
        for block in block_y:
            # 双层循环内的判断
            if not block.left_clicked_flag:
                # 如果当前方块是没有左键点过的
                if block.rect.top <= mouse_y <= block.rect.bottom and block.rect.left <= mouse_x <= block.rect.right:
                    if not block.banner_flag:
                        # 如果不是旗子，可以是问号
                        block.left_clicked_flag = True
                        if status.first_click:
                            # 检测是否是第一次点击的方块
                            block.first_click_flag = True
                        if block.mine_flag:
                            # 如果点开的这个方块是地雷，则加载点开爆炸地雷图片
                            block.image = pygame.image.load(setting.click_mine_block_picture)
                            block.built_me()
                            block.clicked_mine_flag = True
                            status.game_going_flag = False
                        else:
                            # 根据count的数值来加载图片
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
                            elif block.count == 1:
                                block.image = pygame.image.load(setting.picture_1)
                            elif block.count == 2:
                                block.image = pygame.image.load(setting.picture_2)
                            elif block.count == 3:
                                block.image = pygame.image.load(setting.picture_3)
                            elif block.count == 4:
                                block.image = pygame.image.load(setting.picture_4)
                            elif block.count == 5:
                                block.image = pygame.image.load(setting.picture_5)
                            elif block.count == 6:
                                block.image = pygame.image.load(setting.picture_6)
                            elif block.count == 7:
                                block.image = pygame.image.load(setting.picture_7)
                            elif block.count == 8:
                                block.image = pygame.image.load(setting.picture_8)


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
                    elif blocks[y + der_y][x + der_x].count == 1:
                        blocks[y + der_y][x + der_x].image = pygame.image.load(setting.picture_1)
                    elif blocks[y + der_y][x + der_x].count == 2:
                        blocks[y + der_y][x + der_x].image = pygame.image.load(setting.picture_2)
                    elif blocks[y + der_y][x + der_x].count == 3:
                        blocks[y + der_y][x + der_x].image = pygame.image.load(setting.picture_3)
                    elif blocks[y + der_y][x + der_x].count == 4:
                        blocks[y + der_y][x + der_x].image = pygame.image.load(setting.picture_4)
                    elif blocks[y + der_y][x + der_x].count == 5:
                        blocks[y + der_y][x + der_x].image = pygame.image.load(setting.picture_5)
                    elif blocks[y + der_y][x + der_x].count == 6:
                        blocks[y + der_y][x + der_x].image = pygame.image.load(setting.picture_6)
                    elif blocks[y + der_y][x + der_x].count == 7:
                        blocks[y + der_y][x + der_x].image = pygame.image.load(setting.picture_7)
                    elif blocks[y + der_y][x + der_x].count == 8:
                        blocks[y + der_y][x + der_x].image = pygame.image.load(setting.picture_8)
            except IndexError:
                continue


# 当鼠标移动到没有翻开的方块上时作出反应
def response_mouse_position(mouse_x, mouse_y, blocks, setting):
    for block_y in blocks:
        for block in block_y:
            if not block.left_clicked_flag:  # 如果当前方块是没有点过的
                if block.rect.top <= mouse_y <= block.rect.bottom and block.rect.left <= mouse_x <= block.rect.right:
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


# 将地雷列表会知道主屏幕上面去
def update_blocks(blocks):
    for block_y in blocks:
        for block in block_y:
            block.built_me()
