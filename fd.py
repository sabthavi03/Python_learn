n=int(input("Enter the amount you are saving on fixed deposit:"))

m=int(input("Enter savings period in months 3/6/12/36/60:"))




if m==3:
    l=12
elif m==6:
    l=12.5
elif m==12:
    l=13
elif m==36:
    l=14
else:
    l=15

def calculate_interest():
    i=n*l/100*m
    t=n+i
    print("You have a total of RS.",t," in your bank account")


   

calculate_interest()

   
