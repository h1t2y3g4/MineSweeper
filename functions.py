from mouse_class import MouseMove
from mine_block import MineBlock
import sys
import pygame
import pygame.sprite


# 检查事件
def check_event(blocks):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        else:
            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                check_mouse_position(mouse_x, mouse_y, blocks)
        

def check_mouse_position(mouse_x, mouse_y, blocks):
    mouse_class = MouseMove(mouse_x, mouse_y)
    the_block = pygame.sprite.spritecollideany(mouse_class, blocks)
    if the_block:
        the_block.change_mousemotion_flage(False)
        print('碰了')
        print(len(blocks))


def create_blocks(field, screen_main, setting):
    blocks = pygame.sprite.Group()
    block = MineBlock(field, screen_main, setting)
    """
        双层循环填满地雷编组，注意用的是公式。也就是说每次都要创建一个新的地雷实例，然后通过算法直接修改坐标值，每个坐标属性
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
            blocks.add(block)
    blocks.draw(screen_main)