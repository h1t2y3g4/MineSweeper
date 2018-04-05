from mine_block import MineBlock
import sys
import pygame


# 检查事件
def check_event(blocks, setting):
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        else:
            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                response_mouse_position(mouse_x, mouse_y, blocks, setting)
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos
                response_mouse_click(mouse_x, mouse_y, blocks, setting)


# 当鼠标点击了没有翻开的地雷的时候，做出反应
def response_mouse_click(mouse_x, mouse_y, blocks, setting):
    for block in blocks:
        if not block.clicked_flag:
            if block.rect.top <= mouse_y <= block.rect.bottom and block.rect.left <= mouse_x <= block.rect.right:
                block.change_clicked_flag()
                block.image.fill(setting.clicked_mine_block_color)


# 当鼠标移动到没有翻开的方块上时作出反应
def response_mouse_position(mouse_x, mouse_y, blocks, setting):
    for block in blocks:
        if not block.clicked_flag:
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
    """
    for block_number_y in range(block.number_y):
        for block_number_x in range(block.number_x):
            block = MineBlock(field, screen_main, setting)
            block.rect.x = block.field.rect.left + 1 + block_number_x * block.len
            block.rect.y = block.field.rect.top + 1 + block_number_y * block.high
            blocks.append(block)
    return blocks


# 将地雷列表会知道主屏幕上面去
def update_blocks(blocks):
    for block in blocks:
        block.built_me()
