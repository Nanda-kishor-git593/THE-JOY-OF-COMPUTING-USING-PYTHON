#rock-paper -sissor
#3 entites rock, paper,scissor
#paper can cover the rock,but rock can crush the scissor , and socissor can cut the paper
# evriting is equi powerfull
def rock_paper_scissor(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3 #p1 is the place holder for bit postion 1 in num1, we %3 because we want answer in 0,1,2
    p2=int(num2[bit2])%3
    if(player_one[p1]==player_two[p2]):
        print("Draw")
    elif(player_one[p1]=="Rock" and player_two[p2]=="Scissor"):
        print("PLayer_one wins")
    elif(player_one[p1]=='Rock'and player_two[p2]=="Paper"):
        print("Player_two wins")
    elif(player_one[p1]=='Paper'and player_two[p2]=="Scissor"):
        print("Player_two wins")
    elif(player_one[p1]=='Paper'and player_two[p2]=="Rock"):
        print("Player_one wins")
    elif(player_one[p1]=='Scissor'and player_two[p2]=="Rock"):
        print("Player_two wins")
    elif(player_one[p1]=='Scissor'and player_two[p2]=="Paper"):
        print("Player_one wins")

#assigenment for player 1
player_one={0:'Rock',1:'Paper',2:'Scissor'}
player_two={0:'Paper',1:'Rock',2:'Scissor'}
while(1):
    num1=input("Player_one, Enter your choice:")
    num2=input("Player_two, Enter your choice:")
    bit1=int(input("Player_one, Enter the secret Bit Position:"))
    bit2=int(input("Player_two, Enter the secret Bit Position:"))
    rock_paper_scissor(num1,num2,bit1,bit2)
    ch=input("Do you want to continue? y/n")
    if(ch=='n'):
        break


#test cases
#1. 3712,843
#2.584,715