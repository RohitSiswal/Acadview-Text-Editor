#1.a = 3
#if a<4:
 #   a = a/(a-3)
  #  print(a)
#this raises ZeroDivisionError
a = 3
try:
    a = a/(a-3)
except:
    print('Number cannot be divided by zero,try another number')


#2.l = [1,2,3]
#print(l[3])
#this raises IndexError
l =[1,2,3]
try:
    print(l[3])
except:
    print('List index lies in 0-2')

#3.

#try:
 #   raise NameError("Hi there")
#except NameError:
 #   print("An exception")
  #  raise
#output: An exception
#raise doesnot print the parameter

#4.
def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)

# Driver program to test above function
AbyB(2.0, 3.0) #output:-5.0
AbyB(3.0, 3.0)#output:a/b result in 0    as it raises ZeroDivisionError


#5.a.import error

#b.Value error
#i = int(input('Enter an integer')) #input:'abc'
#print(i)     #output:ValueErro
try:
    i = int(input('Enter an integer'))
except:
    print('Entered value is not an integer!Try again.')
#c.Index error
#l = [1,2,3]
#print(l[3])
#this raises IndexError
l =[1,2,3]
try:
    print(l[3])
except:
    print('List index lies in 0-2')

#6.user defined error
class Error(Exception):
    """  """
    pass
class AgeTooSmallError(Error):
    'Age is small!'
    pass
while True:
    try:
        age = int(input('Enter the age'))
        if(age < 18):
            raise AgeTooSmallError
        break
    except AgeTooSmallError:
        print('Entered age is too small')
print('Age is more than 18')