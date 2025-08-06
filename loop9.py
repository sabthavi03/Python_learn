##a=5
##while a>=1:
##    b=1
##    if b==5:
##        print(a)
##    else:
##        print(a,end='')
##    b+=1
##a-=1

##a=5
##while a>=1:
##    b=1
##    while b<=5:
##        if b==5:
##            print(a)
##        else:
##            print(a,end='')
##        b+=1
##    a-=1

a=5
while a>=1:
    b=1
    while b<=5:
        if b!=5:
            print(a,end='')
        else:
            print(a)
        b+=1
    a-=1
