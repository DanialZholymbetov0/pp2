import os
abc = r'C:\Users\PC\Desktop\pp2\githowto\repositories\lab7'
if os.access(abc, os.F_OK):
     print(os.path.basename(abc))
     print(os.path.dirname(abc))
else:
     print("dont exists")