# -*- coding: utf-8 -*-
# 绘制标尺
# 基本情况是标尺为0不打印
# 递归情况是上下的先画减一, 再画当前, 然后在画一个减一的情况.


def draw_line(tick_length, tick_label=''):
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)


def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)


def draw_ruler(num_inches, major_length):
    draw_line(major_length, '0')
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))


if __name__ == '__main__':
    draw_ruler(3, 5)
