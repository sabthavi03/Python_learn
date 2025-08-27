
n=int(input("Enter the number of students in the class:"))
m=int(input("Enter the number of subjects:"))

students=['']

i=0
while i<n:
    if i<n-1:
        students[i]=input("Enter the name of student:")
        students.append("")
    else:
        students[i]=input("Enter the name of student:")
    i+=1
    
#print()
#print(students)


subjects=['']

j=0
while j<m:
    if j<m-1:
        subjects[j]=input("Enter the name of subject:")
        subjects.append("")
    else:
        subjects[j]=input("Enter the name of subject:")
    j+=1
    
print()
#print(subjects)


mark=[]

j=0
while j<m:
    mark.append(0)
    j+=1


marks=[]

i=0
while i<n:
    marks.append(mark.copy())
    i+=1

#print(marks)

i=0
while i<n:
    j=0
    while j<m:
        marks[i][j]=int(input(f"Enter {students[i]}'s marks for {subjects[j]}"))
        j+=1
    print()
    i+=1


#print(marks)


total=[0]

i=0
while i<n:
    if i<n-1:
        total[i]=sum(marks[i])
        total.append(0)
    else:
        total[i]=sum(marks[i])
    i+=1
    

#print(total)


average=[0]

i=0
while i<n:
    if i<n-1:
        average[i]=round(total[i]/m,1)
        average.append(0)
    else:
        average[i]=round(total[i]/m,1)
    i+=1


#print(average)

results=['']

i=0
while i<n:
    if i<n-1:
        if average[i]>=75:
            results[i]="A"
        elif average[i]>=65:
            results[i]="B"
        elif average[i]>=55:
            results[i]="C"
        elif average[i]>=45:
            results[i]="S"
        else:
            results[i]="F"
        results.append('')
    else:
        if average[i]>=75:
            results[i]="A"
        elif average[i]>=65:
            results[i]="B"
        elif average[i]>=55:
            results[i]="C"
        elif average[i]>=45:
            results[i]="S"
        else:
            results[i]="F"
    i+=1


avg=sorted(average,reverse=True)
#print(avg)


a="Student_Name"

print(f"{a:<13}",end='')

for i in subjects:
    print(f"{i:<10}",end='')
    
    
b="Average"
c="Results"
print(f"{b:<7} {c:<8}")

i=0
while i<n:
    x=int(average.index(avg[i]))
    print(f"{students[x]:<13}",end='')

    j=0
    while j<m:
        print(f"{marks[x][j]:<10}",end='')
        j+=1

    print(f"{average[x]:<7}",end='')

    print(f"{results[x]:>5}")
    
    i+=1


























