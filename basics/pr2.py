from unicodedata import name
name = input ("ur name \n")
date = input("date\n")
letter = '''dear nm,
da
glad to say u that u r selected for the interview and nm u can join the conference through ur zoom call.
your manager
aditya raj 
da
'''
letter=letter.replace("nm",name)
letter=letter.replace("da",date)
print(letter)