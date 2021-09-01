cubes = []
for i in range(1, 1001):
    if i % 2 != 0:
        cubes.append(i ** 3)

sum_digit = 0
sum_all = 0
for j in cubes:
    # для решения пунктов b и c - раскомментировать строку ниже
    # j = j + 17
    k = j
    while j != 0:
        sum_digit += j % 10
        j = j // 10
    if sum_digit % 7 == 0:
        sum_all = sum_all + k
    sum_digit = 0
print(sum_all)
