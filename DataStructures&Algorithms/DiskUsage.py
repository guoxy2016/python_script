# -*- coding: utf-8 -*-
import os


def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)
    print(f'{total: <7,}', path)
    return total


if __name__ == '__main__':
    disk_usage('.')
