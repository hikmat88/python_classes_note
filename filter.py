
def checkeven(num):
    return num%2==0


numbers=[3,4,5,6,7,10,15,20,25]
result=list(filter(checkeven,numbers))
print(result)



numbers=[3,4,5,6,7,10,15,20,25]
even_no=[]
odd_no=[]

for num in numbers:
    if num%2==0:
        even_no.append(num)
    else:
        odd_no.append(num)

print('even numbers:',even_no)
print('odd numbers:',odd_no)
