ages=[12,23,34,42,15,87,12,16,25,23,82,57,7,3,2,1,20]
print(ages.count(12))
print(ages.count(70))
print(ages.count(25))
print(ages.count(23))
print(ages)
ages.sort()   # perform in acending order(incresing order)
print(ages)
ages.reverse()   #perform in decending order(decrasing order)
print(ages)

print("---------------------------------------------------")
#student dat set
students = ["Arun","Rajesh","Harish","Akaansha","Lakshmi","Varsha"]
print(students)
students.sort()
print(students)

#for 0th position dummy value
students.insert(0,"JOC")
print(students)

#slicing
#list_name[start:end+1]
#list_name[start_index:end_index+1]
print(students[1:4])
print(students[1:5])
print(students[:])  #defult start=0, and defult end value = end-1
print(students[1:7])
print(students[3:]) #stat from 3 and go up to end
print(students[:5])  # from the begining to 4rth postion
#defult start is =0
#defult end index = length of the list
print(students[2:5])

    



