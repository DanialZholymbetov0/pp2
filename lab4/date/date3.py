import datetime
now=datetime.datetime.now()
now_1=now.replace(microsecond=0)
print(now_1)