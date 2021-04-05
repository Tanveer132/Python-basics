#--------------DICTIONARY--------------

# It is an important datatype used in machine learning 

#key:value

d={1:"Tanveer", 2:"Akshay" ,3:"Shaheem",1:"Kiran"}

#print dictionary
print(d)

#print type of d
print(type(d))

#access the dictionary using key value
print(d[3])

#update the dictionary
d[4]="Snjana"
print(d)


#pop the item in the dictionary
#it pops the last item in the dictionary
d.popitem()
print(d)

#pop the item in the dictionary
#it pops the item at given index
d.pop(2)
print(d)

#TO get the list of the keys, values s
print(d.keys())

#to access the dictionary using for loop
for i in d:
    print(i," => ",d[i])


#to get items in the dictionary.
for item in d.items():
    print(item)

for key,value in d.items():
    print(key,"=>", value)