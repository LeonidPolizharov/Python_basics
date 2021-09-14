from sys import argv
from json import load, loads

with open('bakery.csv', 'a+', encoding='utf-8') as bak:
    if len(argv) == 1:
        bak.seek(0)
        print(bak.read())
    elif len(argv) == 2:
        # print(argv[1])
        bak.seek(0)
        seek_row = bak.readlines()
        print(*seek_row[int(argv[1]) - 1:], end='', sep='')
    elif len(argv) >= 3:
        bak.seek(0)
        seek_row = bak.readlines()
        print(*seek_row[int(argv[1]) - 1:int(argv[2])], end='', sep='')
