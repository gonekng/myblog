import sys
import os

base_path = 'C:\\Users\\user\\Desktop\\강지원\\Github\\myblog\\source\\images\\'
file_path = base_path + sys.argv[1]
file_names = os.listdir(file_path)
print(file_names[0])

i = 0
for name in file_names:
    src = os.path.join(file_path, name)
    dst = str(i) + '.png'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1
