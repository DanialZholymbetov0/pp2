import os
path = os.getcwd()
if os.path.exists("C:/Users/PC/Desktop/pp2/githowto/repositories/lab6/Текстовый документ1.txt"):
  os.remove("C:/Users/PC/Desktop/pp2/githowto/repositories/lab6/Текстовый документ1.txt")
else:
  print("The file does not exist")