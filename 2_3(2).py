temp_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, val in enumerate(temp_list):
    if val[0].isdigit():
        temp_list[i] = '"{:02}"'.format(int(val))
    elif val[-1].isdigit() and int(val) > 0:
        temp_list[i] = '"+{:02}"'.format(int(val))
    elif val[-1].isdigit() and int(val) < 0:
        temp_list[i] = '"{:02}"'.format(int(val))
        print(val)

print(*temp_list)
