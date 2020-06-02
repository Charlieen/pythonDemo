s1 = r'\'hello world\''
s2 = r'\n\\hello,world!\\\n'
s4 = "hello,world"
s3 = """ 

hello,
world!
I come here
"""
print(s1,s2)

ss1 = '\141\142\143\x61\x62\x63'
ss2 = '\u9a86\u660a'
print(ss1,ss2)
print(s3)

# + * in not in [] [:]

s1 = 'hello' * 3
s2 = 'world'

print('ll' in s1)

str2 = ' abc123456 '
print(str2[0])
print(str2[2:5])
print(str2[2:])
print(str2[2::2])
print(str2[::2])
print(str2[::-1])
print(str2[-3:-1])
print(str2.strip())

a,b = 5,10
print('%d * %d = %d' % (a,b, a*b))

print('{0} * {1} = {2}'.format(a,b,a*b))

print(f'{a} * {b} ={a*b}')

for index, elem in enumerate([10,20,30]):
    print(index,elem)

A = ['a','b','c']
A += ['d','e']
A1 = A[1:3]
print(A1)
B =A[:]
print(B)
C= B[::-1]
print(B[::-1])
D =sorted(C)

print(C)
print(D)
print(C)
print('-----')
print(C[::-1])
C.sort(reverse=True)
print(C)

#生成式 和生成器

f = [x for x in range(1,10,2)]
print(f)

f= [x+y+c for x in 'abcde' for y in '12345' for c in 'ABCDE']
print(f)

import sys

f = [x ** 2 for x in range(1,1000)]
print(sys.getsizeof(f))
print(f)

f= (x **2 for x in range(1,1000))

print(sys.getsizeof(f))
print(f)
# for val in f:
#     print(val)

# use yield



