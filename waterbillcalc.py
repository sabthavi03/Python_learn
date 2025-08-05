
n=int(input("Enter the number of litres consumed:"))
a=0
b=3
c=5
d=10

if n>=0:

    if n<=1000:
        a=500
    elif n<=3000:
        a=500+(n-1000)*b
    elif n<=10000:
        a=500+2000*b+(n-3000)*c
    else:
        a=500+2000*b+7000*c+(n-10000)*d
    print("Your water bill is Rs.",a)
    
else:
    print("Invalid Input")



