# the formula of trinagle area
# tri=(a+b+c)/2
# area_tri=(s*(s-a)*(s-b)*(s-c))**0.5

a=int(input('enter the 1st side:'))
b=int(input('enter the 2st side:'))
c=int(input('enter the 3st side:'))
s=float (a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('the area of triangle is %0.2f '%area)