import random
doors=[0]*3
goatdoor=[0]*2 # list used to keep  track of goats 
swap=0 #number of swap wins
dont_swap=0 # number of dont swap wins
j=0
while(j<5):
        x=random.randint(0,2) # xth door will comrise of BMW
        doors[x]="BMW"
        for i in range(0,3):
            if (i==x):
                continue #it will go to the start of the loop   
            else:
                  doors[i]="Goat"
                  goatdoor.append(i)
        choice=int(input("Enter your choice:"))
        door_open=random.choice(goatdoor)  #open a door that comprises of goat
        while(door_open==choice):  #dooropen should'nt be equal to choice made by the participant
             door_open=random.choice(goatdoor)
        ch=input("Do you want to swap ?y/n")
        if(ch=='y'):
            if(doors[choice]=='Goat'):   # means the choice hear contian goat which is initially choosen by player. now he swaped his decition. so obviously another one contain BMW. so he wins
                print('Player wins')
                swap=swap+1
            else:
                print("Player lost")
        else:
                if(doors[choice]=='Goat'):
                    print("Player lost2""")
                else:
                    print("player wins" )
                dont_swap=dont_swap+1
j=j+1
print(swap)
print(dont_swap)


# there are higher probability of win when we swap










