# They can be thought of as  functions which modify the functionality of another function and they
# really help make your code shorter and more pythonic

# def func():
#     return 1
#
# func()
#
# print(func())

# s= 'GLOBAL VARIABLE'
#
# def func():
#     global s
#     # s= 50
#     def f1():
#         return 'f1'
#     print(s)
#     print(locals())
#
# func()
# print(s)
#
# def func2():
#     a=1
#     b='c'
#     print(locals())
#     print(globals()['s'])
#
# func2()

# def hello(name="charlie"):
#     return "hello "+  name
#
# print(hello())
#
# mynewgreet = hello
#
# print(type(mynewgreet))
# print(mynewgreet())
#
# def hello(name = "charlie"):
#
#     print("THE HELLO() FUNCTION HAS BEEN RUN!")
#
#     def greet():
#         return "THIS STRING IN INSIDE GREET()"
#
#     def welcome():
#         return "THIS STRING IN INSIDE WELCOME()"
#     print(greet())
#     print(welcome())
#     print('End of hello()')
#     if name == 'charlie':
#         return greet
#     else:
#         return welcome
#
# # hello()
#
# print(hello('dzg')())


# def hello():
#     return 'Hi charlie'
#
# def other(func):
#     print('hello')
#     print(func())
#
# other(hello)

def new_decorator(func):

    def wrap_func():
        print('CODE HERE BEFORE EXECUTE FUNC')
        func()
        print('FUNC() HAS BEEN CALLED')
    return wrap_func

# def func_needs_decorator():
#     print("THIS FUNCTION IS IN NEED OF A DECORATOR")
#
# func_needs_decorator = new_decorator(func_needs_decorator)
#
# func_needs_decorator()

@new_decorator
def func_needs_decorator2():
    print("THIS FUNCTION IS IN NEED OF A DECORATOR")

func_needs_decorator2()
