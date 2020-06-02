# L: Local - Names assigned in any way within a function (def or lambda),and not decalared golbal in the function
# E:(EFLs)- Name in the local scope of any and all enclosing functions (def or lambda) from inner or outer
# G: (Global) (module) - Names assigned at the top-level of a modle file, or declared global in a def within the file
# B:(Built-in)(Python) - Names preassigned in the built-in names modules: open,range,SyntaxError

x = 25

def my_func():
    x = 50
    # print(x)
    return x

# print(x)
# print(my_func())
my_func()

print(x)

# LOCAL
lambda x: x**2

# Enclosing function locals

name = "This is a global name!"

# so python find the varible is from local =>  enclosing function locals => global =>
def greet():
    name = "sammy"  #

    def hello():
        print("hello " + name)
    hello()

greet()
print(name)


x =50

def func(x):
    print('x is ',x)
    x=1000
    print('local x changed to:',x)

func(x)
print(x)


def func2():
    global x
    x=1000
    # return x;
print('before function call,x is :',x)
func2()

print(x)
