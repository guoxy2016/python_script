# from multiprocessing import Process
#
#
# def func_a():
#     with open('/dev/tty', 'w') as f:
#         f.write('使用ctrl^D结束输入\n')
#     data = open('/dev/tty').read()
#     print('\n', data)
#
#
# if __name__ == '__main__':
#     p1 = Process(target=func_a)
#     p1.start()
import os
os.chmod('more.py', 0b111111100)
