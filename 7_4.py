from collections import defaultdict
import os

root_directory = r'D:\PycharmProjects\Python_Basic\1'
root_files = defaultdict(int)
for root, dirs, files in os.walk(root_directory):
    for i in files:
        file_bytes = os.stat(os.path.join(root, i)).st_size
        power = len(str(file_bytes))
        root_files[10 ** power] += 1

print(sorted(root_files.items()))
for i, j in sorted(root_files.items()):
    print(f'{i}: {j}')
