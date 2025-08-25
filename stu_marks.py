
s=['','','','','']
m=[0,0,0,0,0]
p=[0,0,0,0,0]
c=[0,0,0,0,0]
t=[0,0,0,0,0]
a=[0,0,0,0,0]
r=['','','','','']



i=0
while i<5:
    s[i]=input("Enter student's name:")
    m[i]=int(input("Enter maths marks:"))
    p[i]=int(input("Enter physics marks:"))
    c[i]=int(input("Enter chemistry marks:"))
    t[i]=m[i]+p[i]+c[i]
    a[i]=round(t[i]/3,1)
    print()
    i+=1
    
i=0
while i<5:
    if a[i]>=75:
        r[i]="A"
    elif a[i]>=65:
        r[i]="B"
    elif a[i]>=55:
        r[i]="C"
    elif a[i]>=45:
        r[i]="S"
    else:
        r[i]="F"

    i+=1
        
print()

n="Student Name"
x="Maths"
y="Physics"
z="Chemistry"
w="Total"
u="Average"
v="Results"

print("-"*66)
print(f"{n:<13} {x:<6} {y:<8} {z:<10} {w:<6} {u:<8} {v}")
print("-"*66)

i=0
while i<5:
    print(f"{s[i]:<13} {m[i]:<6} {p[i]:<8} {c[i]:<10} {t[i]:<8} {a[i]:<6} {r[i]}")
    print()
    i+=1
