#the map function allows you to map a function to an iterable object. This means you can call the same function to every itemof an iterable such list

# define function 
def square(num):
    return num**2


# call the function 
mylist=[1,2,3,4,5]
a=map(square,mylist)
print(a)

x=list(map(square,mylist))
print(x)

# define
def check(name):
    if len(name)%2==0:
        return name 
    else:
        return 'odd'

# call the function 
name=['madhab','roshan','manish','ram','shyam']

result=list(map(check,name))
print(result)