import re

# patterns = ['term1','term2']
#
# text = 'This ia a string with term1 ,not not the other!'
#
# for pattern in patterns:
#     print("I'm searching for:"+ pattern)
#
#     if re.search(pattern,text):
#         print('MATCH!')
#     else:
#         print("NO MATCH")
#
# match = re.search('term1',text)
#
# match.start()
# print(type(match))
#
#
# split_term = '@'
# email = 'term@gmail.com'
#
# print(re.split(split_term,email))
#
# print(re.findall('match','test phrase match in match middle'))


def multi_re_find(patterns,phrase):

    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat, phrase))
        print('\n')

multi_re_find(['a','b'], 'hello bob,are you ok?')

multi_re_find(['are','ok'], 'hello bob,are you ok?')

test_phrase = 'sdsd.sdd.sssddd..sdddsddd...dsds...dsssss...sdddd'

# test_patterns =['sd*'] zero or more
# test_patterns =['sd+'] one or more
# test_patterns =['sd?'] either 0 or 1
# test_patterns =['sd{2,3}']
# test_patterns =['s[sd]+'] # after s ,have (one or more) * (s or d)
# some excusion

test_phrase = '12306,This is a string! But is has punctuation. #hashtag How can we remove it?'
# test_patterns = ['[^!.?]+']
# test_patterns =['[a-z]+']

# test_patterns =[r'\d+']
# test_patterns =[r'\D+']
# test_patterns =[r'\s+']
# test_patterns =[r'\S+']
# test_patterns =[r'\w+']
test_patterns =[r'\W+'] # non-alphanumeric

multi_re_find(test_patterns,test_phrase)