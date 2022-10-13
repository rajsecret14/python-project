num1= int(input("enter number 1 : "))
num2= int(input("enter number 2 : "))
num3= int(input("enter number 3 : "))
num4= int(input("enter number 4 : "))

if(num1>num4): #num 1 and num 4 
    f1 = num1
else:
    f1 = num4

if(num2>num3): #num 2 and num 3
    f2 = num2
else:
    f2 = num3

if (f1>f2):
    print(f1,"is greatest")
else:
    print(f2,"is greatest")





