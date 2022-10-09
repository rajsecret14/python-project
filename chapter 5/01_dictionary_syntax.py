mydict = {
    "a": "biillu",   #strings
    "b": "chillu",
    "marks":[1,10,20,20,20], #list
    "tuples": (1,2,3,5,7),   #tuples
    "mydict2" : {  #dictionary in dictionary (nested dictionary)
        "ad" : "twinkle twinkle little star how i wonder what you are ",
        "spc": "you are the most special person of the world."
    },
    1 : 20
}
mydict['a']= [1,2,5,6,4] # we can put anything and anytime (mutable)
mydict["a"] = "billa ullu" #again changed (mutable as many time i can do)
print(mydict)
print(mydict['mydict2']['spc'])
# dict methods
print(mydict.keys()) 
#print only the keys
print(list(mydict.keys())) 
# print keys in list format
print(tuple(mydict.keys()))
#print keys in tuple format
print(mydict.values()) 
#print only the values
print(list(mydict.values()))
#print values in list format
print(mydict.items()) #list[] ki trah hai ye but in form of tuples()
#end