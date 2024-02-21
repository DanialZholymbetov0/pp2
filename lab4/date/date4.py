import datetime
format = "%Y-%m-%d %H:%M:%S"
a_str = input()
b_str = input()
a = datetime.datetime.strptime(a_str, format)
b = datetime.datetime.strptime(b_str, format)
c = b - a
d = c.total_seconds()
print(d)
