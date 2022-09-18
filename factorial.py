num=int(input('enter the number :'))
factorial=1
if num<0:
    print('factorial does not exist')
elif num==0:
    print('the factorial number of 0 is equal to 1')
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print('the factorial of',num, 'is',factorial)
