def remove_split(string,word):
    newstr = string.replace(word,"")
    return newstr.strip()

this = "        harry is best   "
n = remove_split(this,"barry")
print(n)
# confusion