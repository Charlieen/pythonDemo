# print(type((12,2,2)))
# print(type([12,22]))
# print(type(2))
# print(type(1.1))
# print(type(True))

# everthing in Python is an object .

class Dog():

    # CLASS OBJECT ATTRIBUTE
    species = "mammal"

    def __init__(self, color, breed):
        self.breed = breed
        self.color = color

mydog = Dog('black','Lab')

otherDog = Dog('yellow','Zang')

print(type(mydog))
print(mydog)
print(otherDog.color)
print(mydog.color)
print(mydog.species)

class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
    def area(self):
        return self.radius * self.radius * self.pi
        #  return self.radius * self.radius * Circle.pi
    def set_radius(self,radius):
        self.radius = radius


myc = Circle(10)
myc.radius =100;
myc.set_radius(200)
print(myc.area)
print(myc.area()) # self is system auto  compile lever



