import random

#Coded by VEERU
user=int(input("Enter\n 1 for Stone\n 2 for Paper\n 3 for Scissor\n Your Option: "))
comp=random.randint(1,3)
# print(user)
print(f"Computer Option is {comp}")

if (user==comp):
    print("Its a draw")
elif(user==1 and comp==2):
    print("You Loss")
elif(user==2 and comp==3):
    print("You Loss")
elif(user==3 and comp==2):
    print("You Loss")
else:
    print("You Won")