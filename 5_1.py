num = 20


def odd_gen(max_num):
    for i in range(1, max_num + 1, 2):
        yield i


print(odd_gen(num))
print(list(odd_gen(num)))
