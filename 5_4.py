src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

res = [elem for i, elem in enumerate(src[1:]) if elem > src[i]]     # comprehension
res2 = (elem for i, elem in enumerate(src[1:]) if elem > src[i])    # generator

# for i, elem in enumerate(src[1:]):
#     print(i, elem, src[i])
#     if elem > src[i]:
#         res.append(elem)

print(res)
print(list(res2))
