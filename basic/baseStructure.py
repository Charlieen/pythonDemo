# 使用 元组

t = ('zgding',38,True,'beijing')
print(t)
print(t[0],t[3])
for member in t:
    print(member)

t= ('lena',37,False,'beijng')

print(t)
person = list(t)
print(person)

# set
set1 ={1,2,3,3,3,2}
print(set1)
print('Length= ',len(set1))
set2 = set(range(1,10))
set3 =set((1,2,3,3,2,4))
print(set2,set3)

set4 = {num for num in range(1,10) if num%3 ==0 or num % 5==0}
print(set4)

# 使用字典

scores ={'zgding':41,'lean':40,'danile':8}
print(scores)
items1 = dict(one=1,two=2,three=3);
print(items1)
items2 = dict(zip(['a','b','c'],'123'));
print(items2)
items3= {num: num ** 2 for num in range(1,10)}
print(items3)
print(scores['zgding'])
for key in scores:
    print(f'{key}:{scores[key]}')

scores['zgding'] =40
scores['ding'] =90
print(scores)
print(scores.popitem())
print(scores)