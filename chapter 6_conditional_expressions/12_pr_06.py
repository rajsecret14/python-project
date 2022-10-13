m = int(input("enter ur marks\n"))
if m >= 90 and m <= 100:
    print("your grade is - Ex")
elif m >= 80 and m <90:
    print("your grade is - A")
elif m >= 70 and m <80 :
    print("your grade is - B")
elif m >= 60 and m < 70:
    print("your grade is - C")
elif m >= 50 and m < 60:
    print("your grade is - D")
elif m < 50 and m >0:
    print("your grade is - F")
else:
    print("Invalid marks")

