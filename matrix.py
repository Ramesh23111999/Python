n=int(input("enter the number:"))
m=(n+1)/2

for  i in range(1,n):
    for  j in range(1,n):
        if(i==j):
            if(m>i):
                print(n-i+1)
            else:
                print(i)
        elif(n+1==i+j):
            if(m>i):
                print(i)
            else:
                print(j)
        else:
            print(" ")
print("\n")


