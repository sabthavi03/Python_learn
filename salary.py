s=['','','','','','','','','','','','']

i=0
while i<12:
    s[i]=input(f"Enter your salary for month {i+1} :")
    if s[i].isdigit():
        s[i]=int(s[i])
        i+=1
    elif s[i].isalpha():
        while s[i].isdigit():
            s[i]=input(f"Enter your salary for month {i+1}:")
    elif s[i].isspace():
        while s[i].isdigit():
            s[i]=input(f"Enter your salary for month {i+1}:")
print(s)

   
t=['','','','','','','','','','','','']
i=0
while i<12:
    if s[i]<=50000:
        t[i]=s[i]*3/100
    elif s[i]<=100000:
        t[i]=s[i]*5/100
    elif s[i]<=300000:
        t[i]=s[i]*8/100
    else:
        t[i]=s[i]*10/100
    i+=1
print(t)


a=0
for i in s:
    a=a+i
    i+=1

print("Your annual salary is ",a)


b=0
for i in t:
    b=b+i
    i+=1

print("The total tax is ",b)


c=a-b
print("Your Net salary is ",c)

