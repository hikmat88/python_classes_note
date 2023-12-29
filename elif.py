#elif is used to check the multiple condition
a=int(input('Enter the number:'))
if a<0:
    print(a,'is a negative number')

elif a>0:
    print(a,'is a positive number')

else:
    print('zero')

x=10
y=15
z=20
if x>y and x>z:
    print('x is greater')
elif y>z and y>x:
    print('y is greter')
else:
    print('z is greter')