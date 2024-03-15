import os
def abc(path, data):
    with open(path, 'w') as file:
        for item in data:
            file.write(str(item))
path = "C:/Users/PC/Desktop/pp2/githowto/repositories/lab6/Текстовый документ1.txt"
data = ['a', 'b', 'c', 'd']
abc(path, data)
