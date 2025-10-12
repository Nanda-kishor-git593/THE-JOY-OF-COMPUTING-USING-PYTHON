#fizzbuzz
#num = multiple of 3 the person say fizz insted of num. same for 5 multiples he want to buzz.
#if num is multiple of both  3 and 5 (multiples of 15)he/she has to say fizz-buzz 
# if he say multiple of 3  and 5 insted of fizz   or buzz  or fizz-buzz then he/she is out of the game.
#num = 3,6,9,12,18,21,24,27,33 ,36,39,42,---> fizz
#num = 5,10,20,25,35,40,,50--> buzz
#num = 15,30,45 --->fizz-buzz

#approch:
    #first take numbers from 1 to 50.
    #using divisibilty rules make conditions

#0 to 49
# for i in range(50):
 #   print(i)
 
#i wnat 1 to 50
#mistake code
'''for i in range(1,51):
   if(i%3==0):
       print(str(i)+"= Fizz")
   else:
        if(i%5==0):
            print(str(i)+"= Buzz")
        else:
            if(i%3==0 and i%5==0):
                print(str(i)+"= FizzBuzz")
            else:
                print(str(i))
    
        '''
#correct code
 
def fizzBuzz(r):         #function
    for i in range(1,r):
        if(i%3==0 and i%5==0):
            print(str(i)+"= FizzBuzz")
        else: 
                    if(i%3==0):
                            print(str(i)+"= Fizz")
                    else:
                        if(i%5==0):
                            print(str(i)+"= Buzz")
                        else:
                            print(str(i))

fizzBuzz(51)  #calling function


                            
                            