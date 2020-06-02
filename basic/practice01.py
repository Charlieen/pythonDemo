#print(135//10%10)
import random
"""
 find out all  $1^3 + 5^3 + 3^3 = 153$

"""
# for num in range(100,1000):
#     low = num % 10
#     mid = num //10 %10
#     high = num // 100
#     if num == low ** 3 + mid ** 3 + high ** 3:
#         print(num)
# num = int(input('num= '))
# reversed_num =0
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     print(reversed_num)
#     num //= 10
#     print(num)
# print(reversed_num)

# 百钱白鸡问题 求解：

for x in range(0,20):
    for y in range(1,33):
        for z in range(3,100):
            if x+y+z ==100 and 5*x + 3*y + z//3 == 100:
                print('x:%d,y:%d,z:%d' % (x,y,z))
                break

#CRAPS  花旗骰

print(random.randint(1,6))

# money = 1000
# round = 1
#
#
# check = False
# while money>0:
#     count = random.randint(1, 6) + random.randint(1, 6)
#     # first round
#     if count == 7 or count == 11:
#         debt= random.randint(1,500)
#         money += debt
#         print('you win :%d, you have:%d ' % (debt,money))
#     elif count == 2 or count ==3 or count ==12:
#         money -= debt
#         print('you lost :%d, you have:%d ' % (debt, money))
#         # next round
#     else:
#         count_next = random.randint(1, 6) + random.randint(1, 6)
#         while count_next not in (7, count):
#             count_next = random.randint(1, 6) + random.randint(1, 6)
#         if count_next == count:
#             money += debt
#             print('you win :%d, you have:%d ' % (debt, money))
#         elif count_next == 7:
#             money -= debt
#             print('you lost :%d, you have:%d ' % (debt, money))
# print('i have no money')

# ----CRAPS  花旗骰----
#
# from random import randint
#
# money = 1000
# while money >0:
#     print('你的总资产为：',money)
#     needs_go_on = False
#     while True:
#         debt = int(input('请下注: '))
#         if 0< debt <= money:
#             break
#     first = randint(1,6) + randint(1,6)
#     print('玩家摇出了%d点' % first)
#     if first == 7 or first == 11:
#         print('玩家胜!')
#         money += debt
#     elif first == 2 or first == 3 or first == 12:
#         print('庄家胜！')
#         money -= debt
#     else:
#         needs_go_on = True
#     while needs_go_on:
#         needs_go_on = False
#         current = randint(1, 6) + randint(1, 6)
#         print('玩家摇出了%d点' % current)
#         if current == first:
#             print('玩家胜！')
#             money += debt
#         elif current == 7:
#             print('庄家胜！')
#             money -= debt
#         else:
#             needs_go_on = True
#
# print('你破产了，游戏结束！')

"""
    生成前20个 Fibonacci sequence:
"""
x = 1
y = 1
c = 0

for _ in range(2):
    if x == 1 and y == 1:
        print('F:%d,F:%d' % (x, y))
        c = x + y
        y = x
        x = c
    else:
        c = x + y
        y = x
        x = c
        print('F:%d' % (x))

"""
 完美数 6 (6= 1+2+3)
"""

for num in range(1,10, 1):
    acc=0
    index=1
    while index < num:
        if num % index == 0:
            if acc > num:
                break
            else:
                acc = acc + index
                index += 1
        else:
            index += 1

    if acc == num:
        print(num)

""" 
100 以内的所有素数
"""
for num in range(2,100,1):
    index = 1
    while index <= num:
        if num % index == 0 and index not in (1, num):
            break
        else:
            index += 1
            if index == num:
                print(num)
                break
        
