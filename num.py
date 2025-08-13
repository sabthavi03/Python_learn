n=input("Enter your Date of Birth in the form date-month-year:")

if len(n)!=10:
    print("Invalid format")
elif n[2]!="-":
    print("Invalid format")
elif n[5]!="-":
    print("Invalid format")
else:

    a=int(n[0])+int(n[1])
    b=int(n[0])+int(n[1])+int(n[3])+int(n[4])+int(n[6])+int(n[7])+int(n[8])+int(n[9])
    b=str(b)
    c=int(b[0])+int(b[1])
    c=str(c)

    print("Your number is",a)

    if len(c)==2:
        d=int(c[0])+int(c[1])
        print("Your birth number is",d)
    else:
        c=int(c)
        print("Your birth number is",c)    



    
    






    
