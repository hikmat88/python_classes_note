#llop/repeatation/iteration
#repeatation of statement up to specified condition

#for loop

number=[1,2,3,4,5,6,7,8,9,10]
for num in number:
    print(num)

for x in number:
    if x%2==0:
        print('even number are',x)

# total sum 
total =0
for num in number:
    total+=num
    print(total)

for latter in 'programming':
    print(latter)

    # range function 
    for y in range (0,10):
        print(y)

    for a in range(10,101,10):
        print(a)

# nested loop 
color=['yello','orange','red','green']
fruits=['mango','orange','apple','watermelon']

for looks in color:
    for name in fruits:
        print(looks,name)

