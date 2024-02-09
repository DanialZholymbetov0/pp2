def word_frequency(n):
    a={}
    for i in n:
        if i in a:
            a[i]+=1
        else:
            a[i] = 1