1.take input and print
a = []
i = 0
for i in range(0,10):
     b = int(input('Enter a number'))
     a.insert(i,b)
print(a)

2.infinite loop
i = 1
while i>=0:
    print('loop')
    if(i==50):
        break
    i+=1

3.sqaure of prev list
a = []
c = []
i = 0
for i in range(0,4):
    b=int(input('Enter a number'))
    a.insert(i,b)
    c.insert(i,b*b)
print(a)
print(c)

4.store string,ints and floats speratelely
lst = [1,5,8,5.0,4.5,9,'ash','jay']
i = 0
n = []
s = []
f = []
for i in range(len(lst)):
    t=type(lst[i])
    print(t)
    if(t==int):
        n.insert(0,lst[i])
    elif(t==float):
        f.insert(0,lst[i])
    elif(t==str):
        s.insert(0,lst[i])
print(n)
print(s)
print(f)

5.list with even n odd nos.
i = 1
n = 1
l = []
odd = []
even = []
for i in range(102):
    l.insert(0,i)
    i+=1
print(l)
for n in range(0,101,1):
    if(l[n]%2==0):
        even.insert(0,l[n])
    elif(l[n]%2==1):
        odd.insert(0,l[n])
print(even)
print(odd)

6.pattern
i = 1
for i in range(5):
    print('*'*i)

7.user defined dict
dic = {}
i = 0
for i in range(3):
    m = input('enter a key')
    n = input('enter a value')
    dic[m] = n
print(dic)



8.delete an element
i = 0
n = 0
d = []
for i in range(5):
    k=int(input('enter a number'))
    d.insert(0,k)
print(d)
j=int(input('enter another number'))
for n in range(5):
    if(d[n]==j):
        d.pop(n)
print(d)
