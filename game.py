import random
print("welcome to snake water gun game")
l=[ 's','w','g']
chance =10
cha = 0
cp=0
hp=0
while(cha<chance):
    x=input("s for snake,w for water,g for gun")
    y=random.choice(l)
    if (x==y):
        cp=cp+1
        hp=hp+1
        print("game tie one point to each")
    elif(x=='s' and y=='g'):
        cp=cp+1
        print("computer win")
    elif(x=='s'and y=='w'):
        hp=hp+1
        print("human wins")
    elif(x=='w'and y=='s'):
        cp=cp+1
        print("computer wins")
    elif(x=='w'and y=='g'):
        hp=hp+1
        print("human wins")
    elif(x=='g'and y=='s'):
        hp=hp+1
        print("human wins")
    elif(x=='g'and y=='w'):
        cp=cp+1
        print("computer wins")
    else:
        print("wrong input")
    cha=cha+1
    print(f"{chance-cha} is left out {chance}")
print("game over")
if(hp>cp):
    print(f"human wins by {hp-cp}points")
elif(cp>hp):
    print(f"computer wins by{cp-hp}points")
else:
    print("game tie")





