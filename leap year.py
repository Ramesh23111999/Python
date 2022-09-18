year=int(input('Enter the year: '))
if(year%100==0) and (year%400==0):#century year(ending 00)
    print('{}<== this is leap year'.format(year))
elif(year%100 !=0) and (year%4==0):#not century year
    print('{}<== this is leap year'.format(year))
else:
    print('{}<== this is not leap year')