# try block lets you test a block of code of errors
#except block lets you handle the error
# else block lets you execute the code when there is no error
# finally block lets you execute, regardiles of the result of try axcept block

try:
    print(x)

except:
    print('An error occured')

    # multiple except

try:
    print(y)
except NameError:
    print('variable y is not defined')
except:
    print('something went wrong')

# else 
try:
    print(10)
except:
    print('there is a error')
else:
    print('no error')

# finally
try:
    print(a)
except:
    print('a is not define')
finally:
    print('try except block is completed')
