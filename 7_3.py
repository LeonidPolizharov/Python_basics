import os
import shutil

my_proj = 'my_project'

try:
    for root, dirs, files in os.walk(my_proj):
        if 'templates' in dirs and root != my_proj:
            for i in os.listdir(os.path.join(root, 'templates')):
                src = os.path.join(root, 'templates', i)
                dst = os.path.join(my_proj, 'templates', i)
                shutil.copytree(src, dst)

except FileExistsError:
    print('Уже обработано!')
