import random
import string

print("Password Generator")

All_characters = "ABCEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!@#$%^&*_+-="
Length = int(input("Enetr the lenggth of the password :"))
Password = ''.join(random.choice(All_characters)for i in range(Length))
print("Your Password is : ",Password)


