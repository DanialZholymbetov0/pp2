def string_test(abc):
    upper=0
    slower=0
    for i in abc:
        if i.isupper():
            upper+= 1
        elif i.islower():
            slower+= 1
        else:
            pass
    return upper, slower
abc=input()
upper,slower=string_test(abc)
print(upper)
print(slower)