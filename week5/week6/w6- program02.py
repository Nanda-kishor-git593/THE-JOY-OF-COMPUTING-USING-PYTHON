#substitution ciper
import string
#print(string.ascii_letters)
dict = {}
data=""
file=open("D:\Rgukt\Desktop\python\week6\w6- program02_2.txt","w")  # w to open in writing mode
for i in range(len(string.ascii_letters)): # i will sustitue a letter by a its privious letter. so hear key is -1
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
print(dict)
with open("D:\Rgukt\Desktop\python\week6\w6- program02_1.txt") as f :
    while True:
        c=f.read(1)
        if not c:
            print("End of file")
            break
        if c in dict:
            data= dict[c]
        else:
            data=c
        file.write(data)
        print(data)

