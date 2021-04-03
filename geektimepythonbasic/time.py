import datetime

import time

# time
print(time.time())  # 1617422102.53149
print(time.localtime())
# time.struct_time(tm_year=2021, tm_mon=4, tm_mday=3, tm_hour=11, tm_min=55, tm_sec=2, tm_wday=5, tm_yday=93, tm_isdst=0)
print(time.strftime("%Y-%m-%d %H:%M:%S"))  # 2021-04-03 11:55:02

print(datetime.datetime.now())  # 2021-04-03 11:56:07.170541
newtime = datetime.timedelta(minutes=10)
print(datetime.datetime.now() + newtime)  # 在当前时间上 + 10分钟 2021-04-03 12:07:18.262906
newday = datetime.timedelta(days=3)
print(datetime.datetime.now() + newday)  # + 3天 2021-04-06 11:58:19.071643
