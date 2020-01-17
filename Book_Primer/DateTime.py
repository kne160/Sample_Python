'''
Sample of Date & Time
'''

from datetime import date
from datetime import timedelta
from datetime import time
from datetime import datetime

now = date.today()
print(now)

one_day = timedelta(days=1)
tomorrow = now + one_day
print(tomorrow)

noon = time(12, 0, 0)
print(noon)
print(noon.hour)
print(noon.minute)
print(noon.second)
print(noon.microsecond)

now2 = datetime.now()
print(now2)
print(now2.year)
print(now2.month)

import time

now3 = time.time()
print(now3)

now4 = time.ctime(now3)
print(now4)

fmt = "Day: %A, %B %d, %y, Time: %H:%M:%S:%p"
t = time.localtime()
print(t)
print(time.strftime(fmt, t))


