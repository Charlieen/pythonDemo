import random


answer = random.randint(1,100)
counter = 0
while False:
    counter += 1
    number = int(input('please input: '))
    if number < answer:
        print('try to bigger')
    elif number > answer:
        print('try to small')
    else:

        print('good !')
        break
print('你总共猜了%d次' % counter)
if counter >7 :
     print('你的智商明显不足')
### 打印乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d' % (i, j, i*j), end='\t')
    print()

## 求两个整数的最大公约数和最小公倍数。
#x = int(input('x= '))
#y= int(input('y= '))

# if x>y:
#     x,y = y,x
# for factor in range(x,0,-1):
#     if x % factor == 0 and y% factor ==0 :
#         print('%d和%d的最大公约数是%d' % (x,y, factor))
#         print('%d和%d的最小公倍数是%d' % (x,y, x*y//factor))
#         break

#

row = int(input('请输入行数: '))

for i in range(row):
    for _ in range(i+1):
        print('*',end='')
    print()

for i in range(row):
    for j in range(row):
        if j< row-i-1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row-i-1):
        print(' ',end='')
    for _ in range(2*i+1):
        print('*',end='')
    print()
