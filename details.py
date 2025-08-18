fn=input("Enter your first name:")
ln=input("Enter your last name:")
n=input("Enter your Age :")
ic=input("Enter your NIC number :")

while not fn.isalpha ():
    print("Enter the correct name")
    fn=input("Enter your first name:")
    ln=input("Enter your last name:")
    n=input("Enter your Age :")
    ic=input("Enter your NIC number :")

while not ln.isalpha ():
    print("Enter the correct name")
    fn=input("Enter your first name:")
    ln=input("Enter your last name:")
    n=input("Enter your Age :")
    ic=input("Enter your NIC number :")

while not n.isdigit ():
    print("Enter the correct age")
    fn=input("Enter your first name:")
    ln=input("Enter your last name:")
    n=input("Enter your Age :")
    ic=input("Enter your NIC number :")

while not ic.isdigit ():
    print("Enter the correct NIC number")
    fn=input("Enter your first name:")
    ln=input("Enter your last name:")
    n=input("Enter your Age :")
    ic=input("Enter your NIC number :")


y=ic[0:4]
y=int(y)

x=ic[4:7]
x=int(x)

age=2025-y

n=int(n)

if age!=n:
    print("Enter the correct age")
    fn=input("Enter your first name:")
    ln=input("Enter your last name:")
    n=input("Enter your Age :")
    ic=input("Enter your NIC number :")

if x<=500:
    g="male"

    if y%4==0:       #It's a leap year

        if x<=31:
            m=1
            d=x
        elif x<=60:
            m=2
            d=x-31
        elif x<=91:
            m=3
            d=x-60
        elif x<=121:
            m=4
            d=x-91
        elif x<=152:
            m=5
            d=x-121
        elif x<=182:
            m=6
            d=x-152
        elif x<=213:
            m=7
            d=x-182
        elif x<=244:
            m=8
            d=x-182
        elif x<=274:
            m=9
            d=x-244
        elif x<=305:
            m=10
            d=x-244
        elif x<=335:
            m=11
            d=x-305
        else:
            m=12
            d=x-335
    else:

        if x<=31:
            m=1
            d=x
        elif x<=59:
            m=2
            d=x-31
        elif x<=90:
            m=3
            d=x-59
        elif x<=120:
            m=4
            d=x-90
        elif x<=151:
            m=5
            d=x-120
        elif x<=181:
            m=6
            d=x-151
        elif x<=212:
            m=7
            d=x-181
        elif x<=243:
            m=8
            d=x-181
        elif x<=273:
            m=9
            d=x-243
        elif x<=304:
            m=10
            d=x-243
        elif x<=334:
            m=11
            d=x-304
        else:
            m=12
            d=x-334 
else:
    g="female"
    z=x-501

    if y%4==0:       #It's a leap year

            if z<=31:
                m=1
                d=z
            elif z<=60:
                m=2
                d=z-31
            elif z<=91:
                m=3
                d=z-60
            elif z<=121:
                m=4
                d=z-91
            elif z<=152:
                m=5
                d=z-121
            elif z<=182:
                m=6
                d=z-152
            elif z<=213:
                m=7
                d=z-182
            elif z<=244:
                m=8
                d=z-213
            elif z<=274:
                m=9
                d=z-244
            elif z<=305:
                m=10
                d=z-244
            elif z<=335:
                m=11
                d=z-305
            else:
                m=12
                d=z-335

    else:

            if z<=31:
                m=1
                d=z
            elif z<=59:
                m=2
                d=z-31
            elif z<=90:
                m=3
                d=z-59
            elif z<=120:
                m=4
                d=z-90
            elif z<=151:
                m=5
                d=z-120
            elif z<=181:
                m=6
                d=z-151
            elif z<=212:
                m=7
                d=z-181
            elif z<=243:
                m=8
                d=z-181
            elif z<=273:
                m=9
                d=z-243
            elif z<=304:
                m=10
                d=z-243
            elif z<=334:
                m=11
                d=z-304
            else:
                m=12
                d=z-334 

fn=fn.title()
ln=ln.title()
print("Your Full name is ",fn,ln)
print ("Your Date of Birth is ",d,"/",m,"/",y)
print("You are a ",g)
print("You are",age,"years old.")




