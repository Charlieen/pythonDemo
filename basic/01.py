"""
 use variable to keep data and plus abstract times and divided

"""
a = 321
b = 12
print(a + b)
print(a - b)
print(a * b)
print(a / b)

a1 = 100
b1 = 12.34345
c = 1 + 5j
d = 'hello,world'  # str
e = True      # bool

print(type(a1))
print(type(b1))
print(type(c))
print(type(d))
print(type(e))

"""
input() 获取 键盘输入
int() 字符串 转换为 整数

"""
#a11 = int(input('a= '))
# b11 = int(input('b= '))
# print('%d + %d = %d' % (a,b, a+b))

"""
 输入年份，判断闰年
"""
year = int(input('请输入年份：'))
is_leap =  year % 4 == 0 and year % 100 !=0 or year % 400 == 0
print(is_leap)

"""
a b c can be make a three angle ,and then caculate the area
"""
a = float(input('a= '))
b = float(input('b= '))
c = float(input('c= '))

if a+b>c and a+c>b and c+b >a:
    print('周长：%f' % (a+b+c))
    p = (a+b+c)/2
    area = (p*(p-a)*(p-b)*(p-c))** 0.5
    print('面积: %f' % (area))
else:
    print('bu neng ')
