#####################################
#### PART 6: EXERCISE REVIEW  #######
#####################################

# Time to review all the basic data types we learned! This should be a
# relatively straight-forward and quick assignment.

###############
## Problem 1 ##
###############

# Given the string:
s = 'django'

# Use indexing to print out the following:
# 'd'
print(s[0]);

# 'o'
print(s[-1]);

# 'djan'
print(s[:4]);

# 'jan'
print(s[1:4]);
# 'go'
print((s[4:]))

# Bonus: Use indexing to reverse the string


###############
## Problem 2 ##
###############

# Given this nested list:
l = [3,7,[1,4,'hello']]
# Reassign "hello" to be "goodbye"
l[2][2]='goodbye';
print(l)


###############
## Problem 3 ##
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}
print(d1['simple_key']);

d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2']);

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}



print(d3['k1'][0]['nest_key'][1][0]);

###############
## Problem 4 ##
###############

# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]

print(set(mylist))
###############
## Problem 5 ##
###############

# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"




print("Hello my dog's name is {} and he is {} years old".format(name,age));

# control flow
print(1=="1")

if 10<2:
    print('yes!')
    if 2<10:
        print('yes again');

if 10<2:
    print('1<2')
elif 2 == 2:
    print('2==2')
else:
    print('else');


#For Loops

seq =[1,2,3,4,5,5,6];
for item in seq:
    print(item);

d={"sam":30,'charlie':40}

for item in d:
    print(item)
    print(d[item]);

mypairs = [(1,2),(3,4),(5,6)]

for item in mypairs:
    print(item[:1]);

for(a,b) in mypairs:
    print(a+b);

for a,b in mypairs:
    print(a)
    print(b)

i=1;
while i<5:
    print('i is :{}'.format(i))
    i =i+1

print(list(range(0,5,2)))

x = range(10)
for i in x:
    print(i)
print(list(x))

x=[1,2,3,4]

out=[]
for num in x:
    out.append(num**2)

out = [num**2 for num in x]
print(out)

out2= [num**0.5 for num in range(10)]

print(out2)

#functions

def my_func(param1='hello',p2=[]):
    """
    this is the first function of python
    """
    print(param1)
    print(p2)
    return 'hello'

my_func('charlie',[10,20]);

print(my_func())

def addNum(num1,num2):
    return num1+ num2

r1= addNum(1,2);
print(type(r1))
r2= addNum('1','2')
r2= addNum((1,2), (3,4))

 # r2 =addNum({'a':20},{'b':30})

print(r2)
print(type(r2))

#Filter

mylist=[1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2 ==0

evens = filter(even_bool,mylist)

evens =filter(lambda num:num%2==0, mylist)

print(list(evens))

tweet="Go Sports! #Sports"
result = tweet.split('#')[1];
print(result);

print('x' in[1,23,'x'])



