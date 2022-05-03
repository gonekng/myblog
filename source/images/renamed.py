import os

file_path = 'C:\\Users\\SAMSUNG\\Desktop\\myblog\\source\\images\\Setting\\setting_VSCode'
file_names = os.listdir(file_path)

i = 0
for name in file_names:
    src = os.path.join(file_path, name)
    dst = str(i) + '.png'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1
