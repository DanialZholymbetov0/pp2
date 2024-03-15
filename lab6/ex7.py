import os
with open("C:/Users/PC/Desktop/pp2/githowto/repositories/lab6/Текстовый документ.txt", 'r') as a:
    with open("C:/Users/PC/Desktop/pp2/githowto/repositories/lab6/Текстовый документ1.txt", 'w') as b:
        b.write(a.read())
