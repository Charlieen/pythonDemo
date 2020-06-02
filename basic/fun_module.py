from random import randint


def roll_dice(n=2):
    """摇色子"""
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


print(roll_dice(3))


def add(a=0, b=0, c=0):
    return a+b+c


print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))

def add(*args):
    total =0
    for val in args:
        total +=  val
    return total


#print(add(1,2,3,4,5,6))

print('---------')

# 局部作用域，嵌套作用域，全局作用域，内置作用域

def foo():
    global aa
    aa = 200
    a = 200
    b = 'hello'  # 局部作用域 -》 局部变量
    # Pyhton中可以在函数内部在定义函数

    def bar():
        c = True
        print(a)  # 全局作用 域
        print(b)  # 嵌套 作用域
        print(c)  # 局部作用域
        #print      内置作用域

    bar()

if __name__ == '__main__':
    a = 100   # 1 模块内 作用域  =》全局作用域 -》全局变量
    foo()

    aa= 0
    print(a)
    print(aa)
    