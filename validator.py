import random

UID = [["1234567891"], [1234], ["helloWorld"]]
accountNumber = int(input(""))

validUser = False
validPIN = False

attempts = 0

attempts = 3
while attempts > 0:
    inputtedUser = input("")
    if inputtedUser == UID[accountNumber][0]:
        attempts = 0
        validUser = True
    attempts -= 1
