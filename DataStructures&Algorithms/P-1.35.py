"""

"""
import random

nums = range(5, 105, 5)
month = range(1, 13)
day = range(1, 31)
seq = []
for m in month:
    if m == 2:
        for d in range(1, 30):
            seq.append('%2d%2d' % (m, d))
    elif m in [1, 3, 5, 7, 8, 10, 12]:
        for d in range(1, 32):
            seq.append('%2d%2d' % (m, d))
    else:
        for d in range(1, 31):
            seq.append('%2d%2d' % (m, d))

dates = []
for j in range(23):
    date = random.choice(seq)
    if date not in dates:
        dates.append(date)
    else:
        print('有')
