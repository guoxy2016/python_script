# coding=utf-8

import os
import shutil

CHECK_DIR = '/home/guoxy/work/hwcap'
WORK_DIR = CHECK_DIR + '_img'
if os.path.exists(CHECK_DIR):
    shutil.rmtree(CHECK_DIR)
if os.path.exists(WORK_DIR):
    shutil.rmtree(WORK_DIR)


def check_folder(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)


for i in range(1, 10):
    check_folder(WORK_DIR)
    check_folder(WORK_DIR + '/' + '12%s' % i)
    dir1 = WORK_DIR + '/' + '12%s' % i
    for i in range(1, 10):
        check_folder(dir1 + '/' + '2017%s' % i)
        dir2 = dir1 + '/' + '2017%s' % i
        for i in range(1, 10):
            check_folder(dir2 + '/' + '1%s' % i)
            dir3 = dir2 + '/' + '1%s' % i
            for i in range(1, 20):
                file = "%s/%02d" % (dir3, i)
                check_folder(file)
                dir4 = file
                for i in range(3, 15):
                    filen = '%s/camere_hkeied_sdkjf%05d.h265' % (dir4, i)
                    check_folder(filen)

for i in range(1, 10):
    check_folder(CHECK_DIR)
    check_folder(CHECK_DIR + '/' + '12%s' % i)
    dir1 = CHECK_DIR + '/' + '12%s' % i
    for i in range(1, 10):
        check_folder(dir1 + '/' + '2017%s' % i)
        dir2 = dir1 + '/' + '2017%s' % i
        for i in range(1, 10):
            check_folder(dir2 + '/' + '1%s' % i)
            dir3 = dir2 + '/' + '1%s' % i
            for i in range(1, 20):
                file = "%s/%02d" % (dir3, i)
                check_folder(file)
                dir4 = file
                for i in range(3, 18):
                    file = '%s/camere_hkeied_sdkjf%05d.h265' % (dir4, i)
                    file2 = '%s/camere_hkeied_sdkjf%05d.ts' % (dir4, i)
                    if not os.path.exists(file):
                        open(file, 'w').close()
                    if not os.path.exists(file2):
                        open(file2, 'w').close()
