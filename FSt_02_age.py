#find maximum and minimum
a=int(input("Enter the age A: "))
b=int(input("Enter the age B: "))
c=int(input("Enter the age C: "))


# old=max(a,b,c)
# print(old)
# young=min(a,b,c)
# print(young)

if(a>b and a>c):
    print("A is oldest")
    if(b>c and b<a):
        print("B is in the middle")
        print("C is youngest")
    else:
        print("C is in the middle")
        print("B is youngest")
        
    
elif(b>a and b>c):
    print("B is oldest")
    if(a>c and a<b):
        print("A is in the middle")
        print("C is youngest")
    else:
        print("C is in the middle")
        print("A is youngest")
        
    
elif(c>a and c>b):
    print("C is oldest")
    if(a>b and a<c):
        print("A is in the middle")
        print("B is youngest")
    else:
        print("B is in the middle")
        print("A is youngest")
        

