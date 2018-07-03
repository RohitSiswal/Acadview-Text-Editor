#1. leap year or not
yr = int(input('enter the year you want to check'))
if(yr%4 == 0):
    if(yr%100 == 0):
        if(yr%400 == 0):
            print('It is a leap year')
        else:
            print('Not a leap year')
    else:
        print('Not a leap year')
else:
    print('Not a leap year')

#2.sqaure or a rectangle
a = int(input('Enter length'))
b = int(input('Enter breadth'))
c = int(input('Enter length'))
d = int(input('Enter breadth'))
if(a == c and b == d and a is not b):
    print('Rectangle')
elif(a == b and b == c and c== d and d ==a):
    print('Sqaure')

#3.oldest and youngest
x = int(input('enter age of 1st person'))
y = int(input('enter age of 2nd person'))
z = int(input('enter age of 3rd person'))
if(x >= y):
    if(x >= z):
        print('1st is the oldest')
    elif(z >= x):
        print('3rd is the oldest')
else:
    if(y >= z):
        print('2nd is the oldest')
if(x <= y):
    if(x <= z):
        print('1st is the youngest')
    elif(z <= x):
        print('3rd is the youngest')
else:
    if(y <= z):
        print('2nd is the youngest')

#4.prizes based on points
p = int(input('Enter the points scored'))
if(p >= 1 and p <= 50):
    print('"Sorry!No prize this time."')
elif(p >= 51 and p <= 150):
    print('"Congratulations!You won a Wooden Dog"')
elif(p >= 151 and p <= 180):
    print('"Congratulations!You won a Book"')
elif(p >= 181 and p <= 200):
    print('"Congratulations!You won a Chocolates"')

#5.total cost for user
n = int(input('Enter number of units'))
cost = n*100
if(cost < 1000):
    print('Total cost =',cost)
elif(cost >= 1000):
    c = cost * 0.1
    total = cost - c
    print('Total cost =',total)