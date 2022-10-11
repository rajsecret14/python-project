# set method1 - add 
            # set is non repitative
a = {1,5,9,8,6,2,3}
a.add(4)
a.add(4)
a.add(4)
     #kitna bhi add kar lo koi phark nahi padega , ek hi value rahega
print(a)
     # a.add([1,2,3]) list cannot be added because list can be modified but set can't
a.add((1,5,6,8,9,44)) #tuple can be added because tuple can't be modified
print(a)
     # a.add({1:2})   dictionary can't be add because dict can be modified
# method2 - len
print(len(a))
# method3 - remove
a.remove(5)
print(a)
     # length of the set
print(len(a))
     # a.remove(15)    ucant remove because it doesnt exist thats why it will throw error
# method3- pop
print(a.pop()) #remove any arbitrary paart from set
#method4 - clear, makes the set empty
a.clear()
print(a) 


