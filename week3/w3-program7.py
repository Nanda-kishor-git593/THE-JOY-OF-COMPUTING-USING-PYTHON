
# two players in game player-1, player2
# player2 has some word in mind and he shuffel the word and  is shown  to player -1.
#if player -1 find orignal word, he got the point. oterwise other got point.
 # we have to define it using def.(user defined function defined by def)
 
import random
def choose():
     words=['rainbow','computer','science','programming','matematics','player','condition','reverse','water','board']
     pick=random.choice(words)
     return pick
def jumble(word):
   jumbled= "".join(random.sample(word,len(word))) # water --> (-----)(terwa,watre,twera------) , join to joining letters by chosing random letters from word
   return jumbled
def thank(p1n,p2n,p1,p2):
    print(p1n,'your score is :',p1)
    print(p2n,'your score is :',p2)
    print('Thanks for playing')
    print('Have a nice day')
    
    
def play():
    p1name=input("player1, please enter your name:")
    p2name=input("player2, please enter your name:")
    pp1=0
    pp2=0
    turn=0
    while(1):               #while always be true
                #computer's task
                picked_word=choose()
                #create the question
                qn =jumble(picked_word)
                print(qn)
                #at even values  turns pl playing, at odd values of turn p2 paying
               
                #player 1
                if turn%2==0:
                  print(p1name,'your turn')
                  ans = input('what is on my mind?')
                  if ans==picked_word:
                        pp1=pp1+1
                        print('your score is :',pp1)
                  else:
                        print('better luck next time,i thought :',picked_word)
                  c=int(input('press 1 to continue and 0 to quit:'))
                  if c==0:
                      thank(p1name,p2name,pp1,pp2)
                      break  # the corresponding while loop come to end
                        
                #player2
                else:
                     print(p2name,'your turn')
                     ans = input('what is on my mind?')
                     if ans==picked_word:
                         pp2=pp2+1
                         print('your score is :',pp2)
                     else:
                         print('better luck next time,i thought :',picked_word)
                     c=int(input('press 1 to continue and 0 to quit:'))
                     if c==0:
                         thank(p1name,p2name,pp1,pp2)
                         break  # the corresponding while loop come to end
                turn=turn+1
play()
    