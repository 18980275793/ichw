"""wcount.py: count words from an Internet file.

__author__ = "LiaoYinhui"
__pkuid__  = "1700011802"
__email__  = "liaoyijhui@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def wcount(lines, topn=10):
    symbol_list = [',','.','?','!',':','"','(',')',';']
    for n in lines:
        if n in symbol_list:
            lines = lines.replace(n,'')
    lines = lines.lower()
    lst = lines.split(' ')
    sseett = set(lst)
    count_lst = []
    for n in sseett:
        a = lst.count(n)
        count_lst.append((a,n))
    count_lst.sort(reverse = True)
    for n in range(0,topn):
        print(count_lst[n])
    pass

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
