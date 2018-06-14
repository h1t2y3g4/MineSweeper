"""
现在有一个问题是，字体和蒙版都是不断地在增加，是让他们两交替出现避免的重影。
但是一直没有删除，长此以往这两玩意会把内存炸了。
"""
import pygame
import sys


class Status:
    def __init__(self):
        self.ctrl_flag = False
        self.alt_flag = False
        self.rect_list = []
        self.rect_list_position = 0
        self.difficult = 'easy'


def check_event(status):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # ctrl+w退出排行榜
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL):
            status.ctrl_flag = True
        elif event.type == pygame.KEYUP and (event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL):
            status.ctrl_flag = False
        elif status.ctrl_flag and (event.type == pygame.KEYUP and event.key == pygame.K_w):
            pygame.quit()
            sys.exit()
        # alt+F4退出排行榜
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_LALT or event.key == pygame.K_RALT):
            status.alt_flag = True
        elif event.type == pygame.KEYUP and (event.key == pygame.K_LALT or event.key == pygame.K_RALT):
            status.alt_flag = False
        elif status.alt_flag and event.type == pygame.KEYUP and event.key == pygame.K_F4:
            pygame.quit()
            sys.exit()
        # 检测鼠标是否点击了切换排行榜的按钮
        else:
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos
                button = event.button
                if button == 1:
                    if status.rect_list[0].collidepoint(mouse_x, mouse_y):
                        difficult_list = ['easy', 'middle', 'hard', 'very_hard']
                        with open(r'charts/difficult.txt', 'w') as f:
                            f.write(difficult_list[status.rect_list_position])
                        status.rect_list_position += 1
                        if status.rect_list_position >= len(difficult_list):
                            status.rect_list_position = 0


def read_file(status):
    with open('charts/difficult.txt', 'r') as f:
        status.difficult = f.read()
    status.difficult.strip()
    with open('charts/' + status.difficult + '.txt', 'r') as f:
        records = f.readlines()
    records = list(eval(i) for i in records)
    charts = find_top15_record(records)
    return charts, status.difficult


# 找出记录中的前15名
def find_top15_record(records):
    charts = []
    while len(charts) < 15 and len(records) != 0:
        record = min(records, key=lambda x: x['used_time'])
        records.remove(record)
        charts.append(record)
    return charts


# 设置选择难度窗口描述文本
def set_font(screen, font_color, charts, difficult, status):
    difficult_mapping = {'easy': '简单', 'middle': '中等', 'hard': '困难', 'very_hard': '非常困难'}

    # 获得窗口rect信息
    screen_rect = screen.get_rect()

    rect = font_build('点击此处切换排行榜', (screen_rect.right - 100, screen_rect.y + 5), 20, screen, font_color)
    status.rect_list.append(rect)
    font_build(difficult_mapping[difficult] + '榜', (screen_rect.centerx, screen_rect.y + 30), 50, screen, font_color)
    font_build("排名          用时               时间", (screen_rect.centerx - 23, screen_rect.y + 110), 30, screen, font_color)
    begin_rect_y = screen_rect.y + 160
    der_rect_y = 35
    position = 1
    for record in charts:
        # 转换用时格式
        time_unit = '秒'
        if record['used_time'] >= 60:
            minute = int(record['used_time'] / 60)
            second = record['used_time'] % 60
            if minute >= 60:
                hour = int(minute / 60)
                minute = minute % 60
                record['used_time'] = '%d小时%d分钟%d秒' % (hour, minute, second)
            else:
                record['used_time'] = '%d分钟%d秒' % (minute, second)
        else:
            record['used_time'] = str(record['used_time']) + time_unit

        # 循环打印每行的文字
        font_build(str(position), (screen_rect.centerx - 185, begin_rect_y+(position-1)*der_rect_y), 20, screen, font_color)
        font_build(str(record['used_time']), (screen_rect.centerx - 40, begin_rect_y+(position-1)*der_rect_y), 20, screen, font_color)
        font_build(record['local_time'], (screen_rect.centerx + 140, begin_rect_y+(position-1)*der_rect_y), 20, screen, font_color)
        position += 1


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


def main():
    pygame.init()

    status = Status()

    # 初始化程序界面
    screen_main = pygame.display.set_mode((500, 700))
    screen_main.fill((197, 234, 255))
    screen_main_rect = screen_main.get_rect()
    ico = pygame.image.load(r"images/icon.png").convert_alpha()
    pygame.display.set_icon(ico)
    pygame.display.set_caption('排行榜')

    # 绘制一个蒙版，避免字体重叠的问题
    surface = pygame.Surface((500, 700))
    surface.fill((197, 234, 255))
    surface_rect = surface.get_rect()
    surface_rect.topleft = screen_main_rect.topleft

    # 初始化帧数
    fps = pygame.time.Clock()

    while True:
        check_event(status)

        screen_main.blit(surface, surface_rect)

        # 读取文件，绘制到屏幕
        charts, status.difficult = read_file(status)
        set_font(screen_main, (0, 0, 0), charts, status.difficult, status)

        # 绘制

        pygame.display.flip()

        fps.tick(30)


if __name__ == '__main__':
    main()
