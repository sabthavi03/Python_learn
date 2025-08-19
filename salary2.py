m=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

s=[20000,40000,100000,50000,6000,75000,80000,30000,34500,35000,5000,45000]

t=[0,0,0,0,0,0,0,0,0,0,0,0]

i=0
while i<12:
    if s[i]<=50000:
        t[i]=3/100*s[i]
    elif s[i]<=100000:
        t[i]=5/100*s[i]
    elif s[i]<=300000:
        t[i]=8/100*s[i]
    else:
        t[i]=10/100*s[i]
    i+=1

n=[0,0,0,0,0,0,0,0,0,0,0,0]

i=0
while i<12:
    n[i]=s[i]-t[i]
    i+=1

a="Month"
b="Salary"
c="Tax"
d="Net Salary"

print(f"{a:<4}  {b:>10}  {c:>7}  {d:>14}")
print()
i=0
while i<12:
    print(f"{m[i]:<4} {s[i]:>12} {t[i]:>10}  {n[i]:>12}")
    print()
    i+=1
    
print()
print(f"Total      {sum(s)}     {sum(t)}      {sum(n)}")


