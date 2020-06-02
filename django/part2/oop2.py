# INHERITANCE
class Animal():
    def __init__(self,weight=10 ):
        self.weight= weight
        print('Animal created')
    def whoAmI(self):
        print("Animal")
    def eat(self):
        print('eating')

mya = Animal()
mya.whoAmI()
mya.eat()

class Dog(Animal):
    name ='dog'
    def __int__(self):
        Animal.__init__(self)

    def whoAmI(self):
        print("I am Dog ,my Name is {}".format(self.name))
    def specail(self):
        print("I can keep yard")

    def eat(self):
        print("Dog eating")

mydog = Dog( 'sammy')

mydog.whoAmI()
mydog.eat()
mydog.specail()

# SPECIAL
class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages =pages

    def __str__(self):
        return self.title + self.author + str(self.pages)

    def __len__(self):
        return 3;

b= Book('Python','charlie',400)

print(b)
print(len(b))