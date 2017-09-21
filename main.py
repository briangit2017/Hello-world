import time
import datetime as da
import numpy as np

now = da.datetime.now()
print ("Current year: %d" % now.year)
print ("Current month: %d" % now.month)
print ("Current day: %d" % now.day)
print ("Current hour: %d" % now.hour)
print ("Current minute: %d" % now.minute)
print ("Current second: %d" % now.second)
print ("Current second: ", now.second)
print ("Current microsecond: %d" % now.microsecond)
print (now.strftime("%Y-%m-%d %H:%M"))
print (now.isoformat())

start_time = time.time()
time.sleep(1)
elapsed_time = time.time() - start_time
print ("elapsed_time = %d" %  elapsed_time)

import ctypes  # An included library with Python install.
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title",2)

# comment
'''  Styles:
##  0 : OK
##  1 : OK | Cancel
##  2 : Abort | Retry | Ignore
##  3 : Yes | No | Cancel
##  4 : Yes | No
##  5 : Retry | No 
##  6 : Cancel | Try Again | Continue
'''