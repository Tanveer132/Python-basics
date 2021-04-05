#For loop
#for loop works in sequense

# for i in range(5):
#     print("Hello this is number ",i)

#Nested for loop
'''
print("pattern 1")
for i in range(5):
    
    for j in range(5):
        print("*",end=" ")
    print()
'''

#Patterns using for loop
'''
print("pattern 2")
for i in range(5):
    
    for j in range(i+1):
        print("*",end=" ")
    print()
'''

'''
print("pattern 3")
for i in range(5):
    
    for j in range(4-i):
        print("*",end=" ")
    print()
'''

'''
print("pattern 4")
n=4
for i in range(n):
    for j in range(n-i):
        print("",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()
'''

'''
print("pattern 5")
n=4
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()
'''

'''
print("pattern 6")
n=5
mid=int(n/2)
for i in range(n):
    if(i<=mid):
        for j in range(i+1):
            print("*",end=" ")
    else:
        for j in range(n-i):
            print("*",end=" ")
    print()
'''
'''
print("pattern 7")
n=5
mid=int(n/2)
for i in range(n):
    if(i<=mid):
        for j in range(mid-i):
            print(" ",end=" ")
        for k in range(i+1):
            print("*",end=" ")
    else:
        for j in range(i-mid):
            print(" ",end=" ")
        for k in range(n-i):
            print("*",end=" ")

    print()
'''


'''
print("pattern 1")
n=5
for i in range(n-2):
    for j in range(n):
        print("*",end=" ")
    print()
,,,