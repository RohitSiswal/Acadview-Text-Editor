#1.single inheritance
class Animal:#base class
    def animal_attribute(self):
        return('Tiger is an animal')

class Tiger(Animal):#inheriting base class
    def dis(self):
        return('Tiger runs pretty fast.')

a = Tiger()
print(a.dis())
print(a.animal_attribute())

#2.output of the given code
class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print(a.f(), b.f()) #output:A ,B
print(a.g(), b.g()) #OUTPUT:A,B

#3.updating and displaying
class Cop:
    def __init__(self,name,age,work,experience,designation):
        self.n = name
        self.a = age
        self.w = work
        self.e = experience
        self.d = designation

    def display(self):
        return(self.n,self.a,self.w,self.e,self.d)
    def update(self,name,age,work,experience,designation):
        self.n = name
        self.a = age
        self.w = work
        self.e = experience
        self.d = designation
class Mission(Cop):              #inheriting Cop
    def add_mission_details(self):
        return('Adding details')
c = Cop('Amy',35,'Police force','2yrs','Detective')    #displaying
c.update('Amy',35,'Police force','3yrs','Detective')    #updating
print(c.display())


#4.multiple inheritance
class Shape:
    def __init__(self,length,breadth):
        self.l = length
        self.b = breadth
    def Area(self):
        return(self.l * self.b)
class rectangle(Shape):             #inheriting Shape
    def dis(self):
        return('Area of rectangle is')

class square(Shape):            #inheriting Shape
    def dis(self):
        return('Area of square is')

r = rectangle(5,4)
s = square(5,5)
print(r.dis(),r.Area())
print(s.dis(),s.Area())