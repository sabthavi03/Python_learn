
#s={"Maths","Tamil","English","Maths","Science"}       #Unordered,Unique values only
##print(s)
##print(type(s))

##s.add("It")   #To add single values
##print(s)

##s.update("History") 
##print(s)

##s.update(["History","Political Science","Economics"]) #To add multiple values
##print(s)

##s.add(["History","Political Science","Economics"]) #error
##print(s)

##s.remove("Maths")
##print(s)

##s.remove("ABC")     #error
##print(s)

##s.discard("ABC")     #discards if present and don't show error when its not
##print(s)

##s.pop()     
##print(s)

##s.clear()     
##print(s)



#1
##num1=[70,90,70,26,55,40,36,26]
##
##num2=set(num1)
##print(num2)


#2
##a={1,2,3,4,5}
##b={3,5,7,8,9}

#c=a|b          #Union
#c=a.union(b)   #Union
#c=a&b                   #Intersection
##c=a.intersection(b)      #Intersection    
##print(c)

##e=a-b
##print(e)            #{1, 2, 4}


##e=b-a
##print(e)                #{8, 9, 7}

##f=a^b
##print(f)


#3

a={1,2,3}
b={1,2,3,4,5}
c={4,5,6}

d=a|b|c
e=a&b&c

##print("d=a|b|c",d)
##print("e=a&b&c",e)

##print(a<=b)
##print(a.issubset(b))

##print(b.issuperset(a))
##print(b>=a)





























