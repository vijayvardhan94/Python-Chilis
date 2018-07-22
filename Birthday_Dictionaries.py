from random import randint

print ("""Welcome to the birthday dictionary, We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace""")

choice = input("Who's bday do you want to find out?:")
choice = randint(1,3)



birthdays = {
	"Albert Einstein": "14-MAR-1879",
	"Benjamin Franklin": "JAN-17-1706",
	"Ada Lovelace": "10-DEC-1815",
}

if choice == 1:
    print("His bday is on",birthdays["Albert Einstein"])
elif choice == 2:
    print("His bday is on",birthdays["Benjamin Franklin"])
else:
     print("Her bday is on",birthdays["Ada Lovelace"])
    


