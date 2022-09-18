a=int(input('enter the number from: '))
b=int(input('enter the number to: '))
print('prime number is between',a, 'and' ,b, 'are:')
for num in range(a,b+1):
    a=num
    flag=False
    if num>1:
        for i in range(2,num):
            if num%i==0:
                flag=True
                break
        else:
            print(num)
