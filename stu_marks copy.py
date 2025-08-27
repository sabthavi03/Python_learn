
students=['']

n=int(input("Enter how many students are there in your class:"))
m=int(input("Enter how many subjects they are taking :"))


subjects=['']

def get_subjects():
    i=0
    while i<m:
        if i<m-1:
            subjects[i]=input("Enter subject :")
            subjects.append("")
        else:
            subjects[i]=input("Enter subject :")
        i+=1

def get_name():
    i=0
    while i<n:
        if i<n-1:
            students[i]=input("Enter student name :")
            students.append("")
        else:
            students[i]=input("Enter  student name :")
        i+=1

get_subjects()
get_name()


l=[[0]]

i=0
while i<len(students):
    l.extend("[0]")
    i+=1

i=0
while i<len(students):
    if i<len(subjects)-1:
        j=0
        while j<len(subjects):
            if j<len(subjects)-1:
                l[i][j]=input(f"Enter {students[i]}'s marks for {subjects[j]} :")
                l[i].append(0)
            else:
                l[i][j]=input(f"Enter {students[i]}'s marks for {subjects[j]} :")
            j+=1
        l.extend("[0]")
    else:
        j=0
        while j<len(subjects):
            if j<len(subjects)-1:
                l[i][j]=input(f"Enter {students[i]}'s marks for {subjects[j]} :")
                l[i].append(0)
            else:
                l[i][j]=input(f"Enter {students[i]}'s marks for {subjects[j]} :")  
            j+=1
    i+=1


print(l)


