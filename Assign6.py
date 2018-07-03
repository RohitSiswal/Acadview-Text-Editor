1.area of a circle
def area(x):
    return(3.14*x*x)
r = int(input('Enter the radius of the circle'))
print('Area=',area(r))

2.perfect no.
def perfect(x):
    sum = 0
    for i in range(1,x):
        if(x%i == 0):
            sum = sum+i
    if(sum == x):
        return(' perfect')
    else:
        return(' not perfect')
x = int(input("Enter an integer"))
print('Number is',perfect(x))

3.multiplication table of 12
def mul(x,i):
    if(i>10):
        return('0')
    else:
        print(x,'*',i,'=',(x*i))
        return(mul(x,i+1))

i = 1
print(mul(12,i))

4.power of a numberx
def power(a,b):
    if(b == 1):
        return(1)
    elif(b is not 1):
        return(a * power(a,b-1))
n = int(input("Enter an integer"))
m = int(input("Enter the power"))
print(power(n,m))

5.factorial stored in a dict.
def fact(f):
    if(f == 1):
        return(1)
    else:
        return(f*fact(f-1))
a = int(input("enter an integer"))
c = {}
c[a] = fact(a)
print(c)