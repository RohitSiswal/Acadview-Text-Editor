1.time tuple
import datetime
print(datetime.datetime.today())

2.formatted time

import time
sec_obj = time.time()
print(time.ctime(sec_obj))

3.extract month
import time
tup = time.ctime(sec_obj)
print('Month is',tup[4:7])

4.extract day
print('Day is ',tup[:3])

5.extract date
print('Date is ',tup[8:10])

6.local time
import time
print('local time is',time.asctime())

7.factorial
import math

n = int(input('Enter an integer'))
print(math.factorial(n))

8.GCD of a number
import math

g = int(input('Enter an integer'))
h = int(input('Enter an another integer'))
print(math.gcd(g,h))

9.OS package
import os
print('Current worling directory is',os.getcwd())
print('User environment is',os.environ)