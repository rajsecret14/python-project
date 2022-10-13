sub1 = int(input("enter marks of sub 1\n"))
sub2 = int(input("enter marks of sub 2\n"))
sub3 = int(input("enter marks of sub 3\n"))

if (sub1 <33 or sub2<33 or sub3< 33):
    print("you are fail because you have less marks than 33")
elif(sub1+sub2+sub3)/3 < 40:
    print("you are fail due to total percentage less than 40")
else:
    print("congrats\nyou passed this exam.")





