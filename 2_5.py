price_list = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90, 70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29, 8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]
print("A)")
new_price = []
for i in price_list:
    new_price.append('{} руб {} коп'.format(f'{i:.2f}'[:f'{i:.2f}'.index(".")], f'{i:.2f}'[1 + f'{i:.2f}'.index("."):]))
print(", ".join(new_price))

print("B)")
print(price_list)
print('ID до сортировки: {}'.format(id(price_list)))
price_list.sort()
print(price_list)
print('ID после сортировки: {}'.format(id(price_list)))

print("C)")
sorted_price = sorted(price_list, reverse=True)
print(sorted_price)

print("D)")
print(sorted(price_list[len(price_list) - 5:]))
