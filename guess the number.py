import random

target = random.randint(1,100)

while True:
    userChoice = int(input("Guess the target:"))
    
    if(userChoice == target):
        print("Successfull : Correct Guess")
        break
    elif(userChoice <target):
        print("Your number is too small. Take a bigger Guess..")
    else:
        print("your number is too big. Take a smaller Guess..")


print("-----Game over-----")