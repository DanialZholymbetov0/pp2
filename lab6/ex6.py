import os
for i in range(ord('A'), ord('Z')+1):
    name = chr(i) + ".txt"
    f = open(os.path.join("C:/Users/PC/Desktop/pp2/githowto/repositories/lab6", name), 'w')
   