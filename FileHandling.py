#1 Read last n lines of a file.

import os
def Lastline(f,n):
    with open(f) as file:
        print('Last',n,"of file : ",f)
        for line in (file.readline()[-n:]):
            print(line)
name=input("enter file name : ")
n=int(input('number of last lines : '))
try:
    Lastline(name,n)
except:
    print ('error')

#2__count the frequency of words in a file.

file=open("My first commit.txt","r+")

wordcount={}

for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for k,v in wordcount.items():
    print(k, v)

#3__to copy the contents of a file

with open("My first commit.txt") as f:
    with open("first.txt", "w") as f1:
        for line in f:
            f1.write(line)

#4__to combine each line from first file

with open('My first commit.txt') as fh1, open('first.txt') as fh2:
    for line1, line2 in zip(fh1, fh2):
        print(line1+line2)

#5__to perform read and sorting of 10 random numbers
import random
def Rand(start, end, num):
    res = []

    for j in range(num):
        res.append(random.randint(start, end))

    return res
num = 10
start = 30
end = 50
print(Rand(start, end, num))