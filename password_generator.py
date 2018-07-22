import random

charset= 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'
password = ""
for i in range(8):
    password += random.choice(charset)
print(password)
