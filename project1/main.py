import random
# snake water game or rock, paper scissors

def gameWin(comp,you):
    # tie
    if comp == you:
        return None
    # check all the possibilities when comp choose s
    elif comp == 's':
        if you== 'w':
            return False
        elif you == 'g':
            return True
    # comp chooses w
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    #  comp chooses g
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print('computer turn.')
# module is imported
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("your turn: ")
a = gameWin(comp,you)

print(f"computer choose : {comp}")
print(f"you choose : {you}")

if a == None:
    print("the game is a tie.")
elif a:
    print("you win")
else:
    print("you lose!")