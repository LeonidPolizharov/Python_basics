import os

directories = {'my_project':  ['settings', 'mainapp', 'adminapp', 'authapp'],
               'my_project2':  ['settings2', 'mainapp', 'adminapp', 'authapp']}

for i in directories.keys():
    if not os.path.exists(i):
        os.mkdir(i)
    for j in directories.get(i):
        dir_path = os.path.join(i, j)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

