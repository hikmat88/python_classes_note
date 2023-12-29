# lambda expression is used to create the anonymous function, this besically means we can quickly make ad-hoc function without nedding to write def keywoed.

# def square(x):
#     return x**2

square=lambda x: x**2

result=square(4)
print(result)


mylist=[1,2,3,4,5,6,7,8,9,10]
even_no=list(filter(lambda num:num%2==0,mylist))
print(even_no)

result=list(map(lambda num:num**2,mylist))
print(result)