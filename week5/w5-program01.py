#dictionary
   #--> key , value 
#list l =[]
conv_factor={}   # {}denotes dictionary
print(conv_factor)  #print empty dictionary
#i should start adding the conversion factors for various currency sysytems
conv_factor['dollar']=60   #doller is key and 60 is value
print(conv_factor)
conv_factor['euro']=80
print(conv_factor)
#accesing 
print(conv_factor['euro'])
#to acces keys
print(conv_factor.keys())
#in the form of list
print(list(conv_factor.keys()))
#to acces values
print(conv_factor.values())
#in the form of lsit
print(list(conv_factor.values()))
# to access both keysand values simultanously, that's mean we wantto acces what are the items present in the dictionary
print(conv_factor.items())
#items in the form of list
print(list(conv_factor.items()))
conv_factor['dollar']=65   # for updation also
print(conv_factor)
conv_factor['yen']=50
print(conv_factor)
del conv_factor['yen']  #syntax del<space>name_of dictionary['key name (we want to delete)'], if mentioned key is not present in the dictionary the compiler will through key error
print(conv_factor)
euro =30
rupees=euro*conv_factor['euro']
print(rupees)  # 30 *80=2400 means 30 euros is equal to 2400 rupee