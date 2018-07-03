#1.fuction called from a class
class circle(object) :
    def __init__(self,radius):
        self.r = radius
        print(radius)

    def getArea(self):
        return(self.r*self.r*3.14)
    def getCirf(self):
        return(2*3.14*self.r)
x = circle(5)
print(x.getArea())
print(x.getCirf())

#2.display name n roll no.
class Student(object):
    def __init__(self,name,rollno):
        self.n = name
        self.r = rollno
    def display(self):
        return(self.n , self.r)
s = Student( 'Ashita',11601185)
print(s.display())

#3.fahrenheit and celsius
class Temperature(object):
    def __init__(self,celsius,fraht):
        self.c = celsius
        self.f = fraht
    def frah(self):
        return((9/5)*self.c + 32)
    def cels(self):
        return((5/9)*(self.f - 32))
temp = Temperature(0,100)
print(temp.frah())
print(temp.cels())

#4.display and update
class MovieDetails:
    def __init__(self,name,artist,yr_of_rel,ratings):
        self.n = name
        self.a = artist
        self.y = yr_of_rel
        self.r = ratings
    def display(self):
        return(self.n,self.a,self.y,self.r)
    def update(self,nm,art,yr,rate):
        self.n = nm
        self.a = art
        self.y = yr
        self.r = rate
        return (self.n, self.a, self.y, self.r)
mov = MovieDetails('Race 3','Salman Khan',2018,0)
print(mov.display())
print(mov.update('Deadpool 2','Ryan Reynolds',2018,5))

#5.display and claculate
class Expenditure:
    def __init__(self,exp,savings):
        self.e = exp
        self.s = savings
    def display(self):
        return(self.e,self.s)
    def cal(self):
        return(self.e + self.s)
    def dis(self):
        return(self.cal())
exd = Expenditure(1500,1000)
print(exd.display())
print(exd.dis())