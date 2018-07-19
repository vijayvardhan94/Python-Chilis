word = input("enter a word:")
reverse = word[::-1]

print("the word is:", word)
print("the revrerse is:", reverse)

if (word == reverse):
    print("it is a palindrome")
else:
    print("it is not a palidrome")
    