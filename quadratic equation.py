# ax^2+bx+c
# formula  -b +or-(b^2-4ac)^0.5/2a
import cmath
a=int(input('--x^2 enter the number:'))
b=int(input('--x enter the number:'))
c=int(input('-- enter the number:'))
print('{0}x^2+{1}x+{2}'.format(a,b,c))
m=(b**2)-(4*a*c)
ans1=(-b+cmath.sqrt(m))/2*a
ans2=(-b-cmath.sqrt(m))/2*a
print('answer is {0} and {1}'.format(ans1,ans2))