# 1. Single Inheritance

class Animal:
    def sound(self):
        print("animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")


animal=Animal()
animal.sound()

dog=Dog()
dog.sound()

# 2. Multilevel Inheritance

class Vechicle:
    def info(self):
        print("this is a vehicle")

class car(Vechicle):
    def car_info(self):
        print("this is a car")

class ElectricCar(car):
    def battery_info(self):
        print("this is the battery car")



info1=ElectricCar()

info1.info()
info1.car_info()
info1.battery_info()


# 3. Multiple Inheritance Example

class Father:
    def father_trait(self):
        print("Father's trait")

class Mother:
    def mother_trait(self):
        print("Mother's trait")

class Child(Father, Mother): 
        def child_trait(self):
            print("Child's trait")


child = Child()
child.father_trait() 
child.mother_trait() 
child.child_trait()   

# 4. Hierarchical Inheritance Example

class Shape:
    def info(self):
        print("This is a shape")

class Circle(Shape):
    def area(self, radius):
        return 3.14 * radius * radius

class Square(Shape):
    def area(self, side):
        return side * side

circle = Circle()
circle.info()         
print(circle.area(5)) 

square = Square()
square.info()         
print(square.area(4))  


print(Child.__mro__)

