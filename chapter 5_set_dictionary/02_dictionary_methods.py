# dict 1
mydict = {
    "sac": "maann",
    "dac":"chimpanze"
}
# dict 2
mydict3 = {
    "sa":"saurabh",
    "sag":"sagar",
    "sac":"chan" #updates the sac in above dict. (mydict)
}
# method - update the dict.
mydict.update(mydict3) #updates the dictionary with another dict. mydict3 #throwing some error i dont know why 
print(mydict)
# method - items
print(mydict.items())
# method - get , search for value from keys. write only keys
# its throws 'none' if anything is not present in dictionary
print(mydict.get("sac"))
# direct method to find any value from its key
print(mydict['sac']) #but it throws error if key is not present in  dictionary









