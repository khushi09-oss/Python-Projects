import random
print('Rock, paper, scissors!')
rock=1
paper=2
scissors=3
print(1)
print(2)
print(3)
player=(input("choose a number:"))
print('You chose:',player)
computer=random.randint(1,3)
print('computer chose:',computer)
if player==computer:
    print('its a tie!')
elif player==1 and computer==2:
    print('computer won')
elif player==1 and computer==3:
    print('YOU WON')
elif player==2 and computer==1:
    print('YOU WON')
elif player==2 and computer==3:
    print('computer won')
elif player==3 and computer==1:
    print('computer won')
elif player==3 and computer==2:
    print('YOU WON')
else:
    print('try again!')