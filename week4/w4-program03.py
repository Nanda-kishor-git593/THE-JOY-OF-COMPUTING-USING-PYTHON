#leap year
'''
import random
year = random.randint(1993,2018)
print(year)
if(year%4==0 and year%100!=0 or year%400==0):
    print("Given year is a leap year")
else:
    print("Given year is Not a leap year")
   '''

#birthday paradox
#50 people birtday dates randmly
import random
import datetime 
birthday=[]
i=0
while(i<50):
    year=random.randint(1895,2017)#choosen 1895 because oldest person ever leved on earth was 122 years.2017-122=1895
#the oldest person ever leived was 122 years old.
    if(year%4==0 and year%100!=0 or year%400==0):
        leap=1
    else:
        leap=0
    month=random.randint(1,12)
    if(month==2 and leap==1):
       day =random.randint(1,29)
    elif(month==2 and leap==0):
       day =random.randint(1,28)
    elif(month==7 or month==8):
       day=random.randint(1,31)
    elif(month%2!=0 and month<7):
       day=random.randint(1,31)
    elif(month%2==0 and month>7 and month<=12):
       day=random.randint(1,31)
    else:
       day=random.randint(1,30)
    dd=datetime.date(year,month,day)
    day_of_year=dd.timetuple().tm_yday #function for give day_of the year
    i=i+1
    birthday.append(day_of_year)

#sorting:it means arranging the elements in particularly in asending or decending order
birthday.sort()
i=0
while(i<50):
    print(birthday[i])
    i=i+1
    
    
       
      
       