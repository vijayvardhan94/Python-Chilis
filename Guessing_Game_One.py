from random import randint
guess = int(input("enter the nymebr you guessed:"))
random = randint(1,9)
print(random)
if guess == random:
    print("you have guessed it right!")
elif guess < random:
    print("you have guessed it low!")
else:
    print("you have guessed it high!")