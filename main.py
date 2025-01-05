import random

'''
1 for snake
-1 for water
0 for gun

'''

computer = random.choice([-1, 0, 1])

youstr = input("Enter your Choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

print(f"You Chose {reverseDict[you]}\n Computer Chose {reverseDict[computer]}")

if(computer == you):
    print("its draw!")

else:
    if(computer == -1 and you ==1):
        print("You win!")
    elif(computer == -1 and you ==0):
        print("You loose, try again")

    elif(computer == 1 and you ==-1):
        print("You loose, try again")
    elif(computer == 1 and you ==0):
        print("You win!")

    elif(computer == 0 and you == -1):
        print("You win!")
    elif(computer == 0 and you ==1):
        print("You loose, try again")
    
    else:
        print("Something went wrong, Please run again")
    