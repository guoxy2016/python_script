"""
student: Xingyu Guo
"""


def loop(chars='catdog', comp=''):
    if len(comp) == len(chars):
        print(comp)
    for i in chars:
        line = comp
        if i not in line:
            line += i
            loop(chars, line)


loop()
