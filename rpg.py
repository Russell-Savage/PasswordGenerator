import secrets
import string
import sys
import random

print ("")
print ("1. Easy (weaker but eaiser to remember)")
print ("2. Strong (best option most of the time)")
print ("3. Extreme (better write it down/save it, it's gonna be crazy long)")
print ("")

easyChars = string.ascii_letters + string.digits
strongChars = string.ascii_letters + string.digits + string.punctuation

strengthSelect = int(input("Select Password Strength 1-3: "))

#if user chooses extreme password, provide strong password with a random length between 40-60 characters
if strengthSelect == 3:
    passResult = ''.join(secrets.choice(strongChars) for i in range(random.randint(40, 60)))
    print ("Here's your password: ", passResult)
    sys.exit()

#if user enters an invaid number, reset and retry
while strengthSelect < 1 or strengthSelect > 3:
    print("Please choose a number between 1 and 3!")
    strengthSelect = 0
    strengthSelect = int(input("Select Password Strength 1-3: "))


#if user has not chosen option 3(Extreme password), ask how many characters they'd like their pass to be 
if strengthSelect != 3 or strengthSelect < 8:
    passLength = int(input("How long do you want your password to be? (cannot be lower than 8): "))


#if user has entered a password length of less than 8, print warning and and retry
while passLength < 8:
    print("Please choose a number higher than 7!")
    passLength = int(input("How long do you want your password to be? (cannot be lower than 8): "))

#If user selected password strength of 1 or 2, create appropriate type of password and output it to screen
if strengthSelect == 1:
    passResult = ''.join(secrets.choice(easyChars) for i in range(passLength))
    print ("Here's your password: ", passResult)
elif strengthSelect == 2:
    passResult = ''.join(secrets.choice(strongChars) for i in range(passLength))
    print ("Here's your password: ", passResult)
