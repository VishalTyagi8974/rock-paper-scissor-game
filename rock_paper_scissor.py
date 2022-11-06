import random
i=0
l=["rock","paper","scissor"]
human=0
ai=0
while(i<5):
    i=i+1
    a = random.choice(l)
    inp=int(input("press 1 for rock, 2 for paper 3 for scissor"))
    if a=="rock" and inp==1:
        print("tie")
    elif a=="paper" and inp==2:
        print("tie")
    elif a=="scissor" and inp==3:
        print("tie")
    elif a=="scissor" and inp==2:
        print("you loss")
        ai=ai+1
    elif a=="scissor" and inp==1:
        print("you win")
        human=human+1
    elif a=="paper" and inp==1:
        print("you loss")
        ai+=1
    elif a=="paper" and inp==3:
        print("you win")
        human+=1
    elif a=="rock" and inp==2:
        print("you win")
        human+=1
    elif a=="rock" and inp==3:
        print("you loss")
        ai+=1
    else:
        print("invalid input")

if human>ai:
    print("you won the game")
elif human<ai:
    print("you loss the game")
elif human==ai:
    print("match tie")

exit=input()