from itertools import zip_longest
from json import dump

user_hobby = {}
with open('users.csv', 'r', encoding='utf-8') as u, open('hobby.csv', 'r', encoding='utf-8') as h:
    if sum(1 for line in u) > sum(1 for line in h):
        u.seek(0)
        h.seek(0)
        for i, j in zip_longest(u, h):
            if j is None:
                user_hobby[i.replace(',', ' ').replace('\n', '')] = j
            else:
                user_hobby[i.replace(',', ' ').replace('\n', '')] = j.replace('\n', '')
        with open('user_hobby.csv', 'w') as uh:
            dump(user_hobby, uh)
    else:
        exit(1)

print(user_hobby)

