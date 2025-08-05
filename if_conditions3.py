
#Current bill calculator

n=int(input("Enter the number of units consumed:"))

if n>0:
    if n<=90:
        print("Your current bill is Rs.",n*7)
    elif n<=150:
        print ("Your current bill is Rs.",90*7+(n-90)*10)
    elif n<=300:
        print("Your current bill is Rs.",90*7+60*10+(n-150)*15)
    else:
        print("Your current bill is Rs.",(90*7+60*10+150*15+(n-300)*15)+(90*7+60*10+150*15+(n-300)*15)*0.03)

else:
    print("Invalid Input")


