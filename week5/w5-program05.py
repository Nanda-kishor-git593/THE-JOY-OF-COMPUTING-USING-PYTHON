#binary search

#sorting-->bubble sort
#bobble sort:
#array=5,1,4,2,8
#i need final after
#  sorting: array=1,2,4,5,8
#1st iteration: compare 5 and 1. 5  is not less than 1, so i will make swap-->1,5,4,2,8 again foe 5 and 4--->1,4,2,5,8next 5,and 2-->1,4,2,5,8next 5 and 8 -->no swap needed.
#end of first iteration i will got 1,4,2,5,8

#2nd iteration: again same i will perform
#finally i will get-->1,2,4,5,8
def bubble(a):
    n=len(a)

    for i in range(n):    #i for iteartions
        for j in range(0,n-i-1):  #-i for when the maximum element gets to its last position, so we have to exclude taht element, and -1 for maintaining proper indexing
            if(a[j]>a[j+1]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp

a=[5,1,4,2,8]
bubble(a)
for i in a:
    print(i)
