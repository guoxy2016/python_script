# coding=utf-8
import logging
import os

CHECK_DIR = '/home/guoxy/work/hwcap'
WORK_DIR = CHECK_DIR + '_img'
# 设置日志
logging.basicConfig(
    level=logging.INFO,
    filename='./errlog.log',
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger()


# 获取文件夹
def work_inner_folder(folder):
    fol_list = os.listdir(folder)
    ret_list = []
    for fol in fol_list:
        if os.path.isdir(folder + '/' + fol):
            if fol.endswith('.h265'):
                ret_list.append(folder + '/')
                break
            else:
                ret_list.extend(work_inner_folder(folder + '/' + fol))
    return ret_list


def work_first_folder(folder):
    result_list = []
    fol_list = os.listdir(folder)
    for fol in fol_list:
        path1 = folder + '/' + fol
        fol1_list = os.listdir(path1)
        for fol1 in fol1_list:
            if fol1.endswith('-ok'):
                path2 = path1 + '/' + fol1
                middle_list = work_inner_folder(path2)
                result_list.extend(middle_list)

    return result_list


work_folder_list = work_first_folder(WORK_DIR)
delete_file_list = []

# 遍历文件夹, 按照对应关系找出应当删除的文件
for work_folder in work_folder_list:
    h265_file_list = os.listdir(work_folder)
    h265_file_list = [i.rsplit('.', 1)[0] for i in h265_file_list]
    check = work_folder.replace(WORK_DIR, CHECK_DIR, 1)
    check = check.replace('-ok/', '/', 1)
    if os.path.exists(check):
        check_file_list = os.listdir(check)
        for check_file in check_file_list:
            # print(check_file)
            if check_file.rsplit('.', 1)[0] not in h265_file_list:
                delete_file_list.append('%s%s' % (check, check_file))
            if check_file.find('.') == -1:
                delete_file_list.append('%s%s' % (check, check_file))
    else:
        print('%s没有找到对应文件夹' % check)
        logger.error('%s没有找到对应文件夹' % check)

# 将被删除的文件保存到文件里
with open('delete_file.txt', 'w') as f:
    for dele in delete_file_list:
        f.write("%s\n" % dele)

# 删除文件
for i in delete_file_list:
    print('删除文件:%s\t' % i)
    try:
        os.remove(i)
        print('删除成功')
        logger.info('%s删除成功' % i)
    except Exception as e:
        print('\n删除失败')
        logger.error('%s删除失败' % i)
        logger.error(e)
        print(e)
