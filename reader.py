# # print('got this: "%s"' % input())
# # import sys  # noqa
# #
# # # print(sys.stdin.readlines())
# # data = sys.stdin.readline().strip()
# # # data = input()
# # print('the meaning of life is ', data, int(data) * 2)
#
# import re  # noqa
#
# c = re.compile(r"[ugoa]*([-+=]([rwxXst]*|[ugo]))+|[-+=][0-7]+")
#
# print(c.match('777') is None)
#
#
#
import os
import subprocess
import sys

subprocess.run(['ls', '-al'], stdout=subprocess.PIPE)
out_list = os.pipe().readlines()
print(out_list)
print(len(out_list))


