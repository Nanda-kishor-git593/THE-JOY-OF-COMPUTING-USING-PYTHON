#Lists : flexible data stucture, where we can add and delete elements

shopping = ["Bread","Coffee","Suger"]
print(shopping)


for i in range(3):
    print(i)
#I just want name of elements in one by one
for item in shopping:
    print(item)
    
print(shopping)
#append == adding to the end of the list
shopping.append("Curd")
shopping.append("shampoo")
print(shopping)


#lec-2
#manipulation

#index (position holder): the counting start from 0

print(shopping[1])
print(shopping[0])
print(shopping[2])
print(shopping[3])

print("using for loop :")
for item in range(5):
    print(shopping[item])


#insert():used to insert elements at needed position using index
print("after insert:")
shopping.insert(1,"oil")
for item in shopping:
    print(item)

#count()
ages = [12,23,34,15,87,12,16,25,23,82,57,7,3,2,3,1,20]
print("no of persons of age 25:",ages.count(25))
print("no of persons of age 12:",ages.count(12))
print("no of persons of age 70:",ages.count(70))

#len()
print("length of ages list :",len(ages))
print("length of shopping list :",len(shopping))


#using of len()

for i in range(len(shopping)):
    print(shopping[i])
print(shopping)
for item in shopping:
    print(item)
    


