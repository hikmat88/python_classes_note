# function -> a block of code to perform the particular task
# function is reusable
# call the function using parenthesis() eg: demo()
# define the function using def eg def demo():....


#define the function
def demoFunction():
    print('This is a function') 


# call the function
demoFunction()



# define with argument
# define the function
def addFunction(x,y):
    sum=x+y
    print('The sum is',sum)

# function with arguments
addFunction(20,30)


# function with return type

# define 
def testFunction(num1,num2):
    data=num1*num2
    return data

# call the function
result=testFunction(5,10)
print('The result is',result)
test=testFunction(5,4)
print(test)


# define
def checkFunction(x):
    if x%2==0:
        return 'even number'
    else:
        return 'odd number'

# call the function
check=checkFunction(10)
print(check)