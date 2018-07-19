from random import randint
print("enter r for rock, p for paper,and s for scissors")
player = input('rock(r), paper(p), scissors(s)')
print(player, "versus:")
chosen = randint(1,3)
#print(chosen)

if chosen == 1:
    computer = 'r'
elif chosen == 2:
    computer = 'p'
else :
    computer = 's'
print(computer)

if player == computer:
    print("game drawn")
    