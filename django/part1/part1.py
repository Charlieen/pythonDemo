print('hello world');
print(2+ 10* 10 +5);
a =5
a= a**2;

# comment
twoDogs = 'hello';
print(twoDogs);
print(a);

print(" I'm a dog");

mystring = 'abcdefg';
print(mystring[2:]);

print(mystring[4:]);

print(mystring[:3]);

print(mystring[2:5]);  # left open ,right close

print(mystring[:]);

print(mystring[::]);
print(mystring[::2]);
print(mystring[::1]);
print(mystring[::3]);
print(mystring[::4]);

x= mystring.upper();
y= mystring.capitalize()
print(y)

print(mystring.split())
# mystring[0]='X';


mystring = 'hello world';
x = mystring.split(' ');
x= mystring.split(('e'));
x= mystring.split('o')
print(x)

x= "Insert another string here:{}".format("INSERT ME!")
x= "Item one:{} Item two:{}".format('dzg',"cat")
x= "Item one:{x} Item two:{x}".format(x='dzg',y= "cat")
print(x);

# List;

mylist=[1,2,3,4];
#mylist=['hello',1,2,[1,2,4]];
print(len(mylist))
print(mylist[-1])
print(mylist[:3])
mylist[0]='hello world';
print(mylist);


mylist.append(5);
#mylist.append(['a','1','b',[1,2,3]]);
mylist.extend(['1','1',[1,2,3,4]]) # just one layer
print(mylist);

mylist=['a','b','c','d','e'];
mylist.reverse()
print(mylist);
item =mylist.pop(1);
print(mylist)
print(item);

mylist=[1,23,34,2,5,66];
mylist.sort()
print(mylist)

mylist=[1,2,3,['x','y',['a','b','c']]];
print(mylist[3][2][0]);

matrix = [[1,2,3],[4,5,6],[7,8,9]];

# LIST Comprehension
first_col = [row[0] for row in matrix];
first_row = matrix[0];
print(first_col)
print(first_row)

# dictionary
my_stuff ={"key1":{'12':[1,2,'gram']},"key2":"value2","key3":[1,2]}

print(my_stuff['key1']['12'][2].upper())

my_stuff = {'lunch':'pizza','bfast':'egg'};
my_stuff['lunch'] = 'dabing';
my_stuff['dinner'] = 'fish';

print(my_stuff)

# Tuples Sets and Booleans
# Tuples is immutable;
True
False

t= (1,2,3);
t=('a',True,124,[1,2])

# t[0]='A';
#
# t=[1,23,4];
# t[0]=1000;

print(t[:2])

x= set([3,3,3,3,4,4,4,4,])
x.add(1)
x.add(2)
print(x)