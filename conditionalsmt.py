#condition statement is used to check whether the condition is met or not

# if else
# elif

x=int(input('Enter the value of x:'))
if x%2==0:
    print(x,'is an even number')
else:
    print(x,'is an odd number')
year=int(input('Enter the year to check if leap year or not'))
if (year%4==0 and year%100!=0) or year%400==0:
    print(year,'is a leap year')
else:
    print(year,'is not leap year')

#write a program to check if a particular number is multiple of 5 or not
if 15%5==0:
    print('multiple of 5')
else:
    print('not a multiple of 5')

    
