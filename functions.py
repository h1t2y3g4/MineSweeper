from mine_block import MineBlock
import sys
import pygame
import random


# 检查事件
def check_event(blocks, setting, status):
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
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
                        pass
            else:
                open_other_block(blocks, setting)


def open_other_block(blocks, setting):
    for block_y in blocks:
        for block in block_y:
            if block.mine_flag and not block.clicked_mine_flag:
                block.image = pygame.image.load(setting.other_mine_block_picture)


# 当鼠标点击了没有翻开的地雷的时候，做出反应
def response_mouse_left_click(mouse_x, mouse_y, blocks, setting, status):
    for block_y in blocks:
        for block in block_y:
            # 双层循环内的判断
            if not block.clicked_flag:
                # 如果当前方块是没有点过的
                if block.rect.top <= mouse_y <= block.rect.bottom and block.rect.left <= mouse_x <= block.rect.right:
                    block.change_clicked_flag()
                    if block.mine_flag:  # 如果点开的这个方块是地雷，则加载点开爆炸地雷图片
                        block.image = pygame.image.load(setting.click_mine_block_picture)
                        block.built_me()
                        block.clicked_mine_flag = True
                        status.game_going_flag = False
                    else:
                        block.image.fill(setting.clicked_mine_block_color)

    if status.first_click:
        # 第一次点击以后再生成地雷
        create_mines(blocks, setting)
        status.first_click = False


# 当鼠标移动到没有翻开的方块上时作出反应
def response_mouse_position(mouse_x, mouse_y, blocks, setting):
    for block_y in blocks:
        for block in block_y:
            if not block.clicked_flag:  # 如果当前方块是没有点过的
                if block.rect.top <= mouse_y <= block.rect.bottom and block.rect.left <= mouse_x <= block.rect.right:
                    block.image.fill(setting.mine_block_color_mousemotion)
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


# 在小方块中生成地雷
def create_mines(blocks, setting):
    mine_count = 0
    number_x = blocks[0][0].number_x
    number_y = blocks[0][0].number_y
    while mine_count < setting.mine_number:
        rand_x = random.randint(0, number_x - 1)
        rand_y = random.randint(0, number_y - 1)
        if not (blocks[rand_y][rand_x].clicked_flag or blocks[rand_y][rand_x].mine_flag):
            blocks[rand_y][rand_x].mine_flag = True
            mine_count += 1


# 将地雷列表会知道主屏幕上面去
def update_blocks(blocks):
    for block_y in blocks:
        for block in block_y:
            block.built_me()
