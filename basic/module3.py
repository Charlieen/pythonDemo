def foo():
    pass

def bar():
    pass

# __name__ 是python 中一个隐含的变量 它代表了模块的名字
# 只要被 python解释器直接执行的模块的名字才是 __main__


if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()