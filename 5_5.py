src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

res = [val for val in src if src.count(val) == 1]

print(res)

# result = [23, 1, 3, 10, 4, 11]

src2 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

res2 = set()
temp = set()
for val in src2:
    if val not in temp:
        res2.add(val)
    else:
        res2.discard(val)
    temp.add(val)
res2_sorted = [val for val in src2 if val in res2]

print(res2_sorted)
