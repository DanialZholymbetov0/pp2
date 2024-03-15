import os
path = r'C:/Users/PC/Desktop/pp2/githowto/repositories/lab6/Текстовый документ.txt'
with open(path, 'r') as f:
    lines = f.readlines()
    print('Number of lines in {}: {}'.format(os.path.basename(path), len(lines)))
