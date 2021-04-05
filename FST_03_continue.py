#To change the flow of the loops, We use 
''' 
    1. break
    2. continue
'''

'''
for i in range(5):
    if i==3:
        print("3 is found.")
        continue
    print(i)
'''

i=0
while(i<5):
    i+=1
    if i==3:
        print("3 is found.")
        continue
    print(i)