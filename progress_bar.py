# -*- coding: UTF-8 -*-

# https://stackoverflow.com/questions/43515165/pycharm-python-console-printint-on-the-same-line-not-working-as-intended
# Works in console and in PyCharm IDE

import sys
import time

progressVis1 = {
    0:  '          ',
    1:  '-         ',
    2:  '--        ',
    3:  '---       ',
    4:  '----      ',
    5:  '-----     ',
    6:  '------    ',
    7:  '-------   ',
    8:  '--------  ',
    9:  '--------- ',
    10: '----------',
}

progressVis = {}
for n in range(0, 51):
    s = '-' * n + ' ' * (50 - n)
    progressVis[n] = s

size = 2000
for i in range(0, size):
    percent = int((float(i + 1) / size) * 50)
    str1 = "\r \r [{0}] {1}/{2} {3}%".format(progressVis[percent],
                                             i + 1, size,
                                             ((i + 1) * 100 / size))
    sys.stdout.write(str1)
    sys.stdout.flush()
    time.sleep(0.002)
