import os 
   #Files and directories
print( os.getcwd())  
with os.scandir(os.getcwd()) as abc:
    for i in abc: 
            print(i)
   #Directories
abc = [i.name for i in os.scandir(os.getcwd()) if i.is_dir()]
for i in abc:
    print(i)            
    #Files
with os.scandir(os.getcwd()) as abc:
    for i in abc: 
        if not i.is_dir():
            print(i.name)   