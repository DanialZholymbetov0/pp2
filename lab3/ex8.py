def fibbonachi(a):
    if a <= 1:
        return a
    else:
        return(fibbonachi(a - 1) + fibbonachi(a - 2))
    
n = int(input())
for i in range (n):
 print(fibbonachi(i))