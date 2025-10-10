


'''
with open("file1.txt","r+") as myfile:    # w - writing mode.r+ both read and write mode
    print(myfile.read())                  # r-read mode
    myfile.write("I am fine")          
myfile.close()   
'''

# random library
#is basically used to genarate random numbers
'''
import random
print(random.randint(1,5))
print(random.randrange(1,5)) # it not genrate 5 . (1 to 4)gnarate
print(random.random()) # genarate decimal numbers from 0 to 1
print(random.randrange(1,10,2))#2 us like step genatere random  odd numbes like 1,7,9,3,5
print(random.randrange(2,10,2))# in 1st is 2 to get even ,2 us like step genatere random  even  numbes like 4,8,6,2
print(random.choice([1,2,3,4])) # genarate random numbers from specified list
mylist = [11,45,67,89]
print(random.choice(mylist))
'''

#progarm of evolution
# pic a digit randomly from binry sequence. if the picked digit is 0 make it 1.
#enventually total binary sequence become 1
#evelution: change in things by successive genarations
#evloution happend by using dna
import random
def evolve(x):            #ind--index
    ind = random.randint(0,len(x)-1) #upper limit and lower lmit in range are inclusive
    p = random.randint(1,100)
    print(p)
    if (p==1):
        if(x[ind]=='0'):
            x[ind]=='1'
        else:
            x[ind]=='0'
    
with open("filedna.txt") as myfile:
    x=myfile.read()
    x=list(x)
for i in range(0,368):
    evolve(x)
print(x)