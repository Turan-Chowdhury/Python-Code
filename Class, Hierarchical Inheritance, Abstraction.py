'''
 1. method without body is an abstract method
 2. class having abstract method is an abstract class
 3. abstract class can not have objects
 4. subclasses must have the abstract methods with the same name that have defined super class
'''

from abc import ABC, abstractmethod

class Shape(ABC) :
    def __init__(self, dim1, dim2) :
        self.dim1 = dim1
        self.dim2 = dim2

    @abstractmethod
    def area(self) :M
        pass

class Triangle(Shape) :
    def area(self) :
        print("Area = ", 0.5 * self.dim1 * self.dim2)

class Rectangle(Shape) :
    def area(self) :
        print("Area = ", self.dim1 * self.dim2)

t = Triangle(20,30)
t.area()

r = Rectangle(20,30)
r.area()
