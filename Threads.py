#1.delays the message for 5secs
import _thread as thread
import time

def display(t,delay):
    i = 0
    while i<3:
        time.sleep(5)
        print('%s after %d secs delay'%(t,delay))
        i +=1
thread.start_new_thread(display,('Thread1',5))
while True:
    pass

#2.1-10 after 1 sec
import _thread as thread
import time

def t_print(t,d):
    for i in range(1,11):
        time.sleep(1)
        print(i)
    print('%s after %d delay'%(t,d))
thread.start_new_thread(t_print,('thread1',1))
while True:
    pass

#3.delay goes like 2sec-4sec-6sec-8sec
import threading
import time
def delay(r,i):
    for i in range(1,6):
            time.sleep(i*2)
            m = lst[i-1]
            print('%s shows the %d element:%s'%(r,i,m))

lst = ['a','b','c','d','e']
t = threading.Thread(delay('Thread1',1))

#4.factorial function using thread
import _thread as thread
import math

def fct(p,n):
    f = math.factorial(n)
    print('%s shows factorial of %d,which is:'%(p,n))
    print(f)
thread.start_new_thread(fct,('thread',5))
while True:
    pass