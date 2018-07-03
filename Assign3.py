1.Length of tuple
a = (1,2,3,4,55,'length')
print('Lenght =',len(a))

2.Largest and smallest in tuple
b = (55,23,6,89,0)
print('Largest is',max(b),'and','smallest is',min(b))

3.product of all elements
c = (5,4,8)
l = len(c)
i=0
f=1
for i in range(l):
    f  = f*(c.__getitem__(i))
    i+=1
print(f)

#unpacking
tup = (1,2,3,4,5)
a,b,c,d,e = tup
print(a)
print(b)
print(c)
print(d)
print(e)

#SETS
#1.diff btw 2 sets
x = {1,2,4,65,6}
y = {5,6,98,7}
print()

4.create a dict
dit = {"Name":"Rohit","Age":20}
print(dit)

5.Sort a dict
dit = {1:'keys',5:'values',4:'sorted',3:'keys'}
li = list(dit.values())
li.sort()
print(li)
ls = list(dit.items())
ls.sort()
print(ls)

6. occurence of each letter
c = {}
m = ['M','I','S','S','I','S','S','I','P','P','I']
for i in range(len(m)):
    j = m[i]
c['M'] = m.count('M')
c['I'] = m.count('I')
c['S'] = m.count('S')
c['P'] = m.count('P')
print(c)