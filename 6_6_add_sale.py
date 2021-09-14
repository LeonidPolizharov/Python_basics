from sys import argv
from json import dumps, dump, load, loads

with open('bakery.csv', 'a+', encoding='utf-8') as bak:
    sum_row = argv
    bak.write(argv[1] + '\n')
    print(argv)
