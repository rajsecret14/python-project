mydict = {
    "pankha":"fan",
    "roshni":"light",
    "kitab":"book",
    "ghadi":"clock"
}
print(mydict.keys())
a = input("enter a word ")
# print("meaning",mydict[a])  it will throw error,if key is not present .
# it doesn't throws error, get(a)
print("meaning",mydict.get(a))
