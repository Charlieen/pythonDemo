try:
    f = open('simple2.txt', 'r')
    f.write("Test write to simple text!")
except:
    print("Error:COULD NOT FOUND FILE OR READ DATA!")
else:
    print('Success')
    f.close()
print('hello world')


try:
    f= open('he.txt','w')
    f.write("heloo helloo")
except:
    print('error')
finally:
    print('I ALWAYS WORK NO MATTER WHAT!')