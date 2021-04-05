#membership operator

'''
l=[1,3,4,5,6.6,"hello","t"]
a=int(input("Enter your search :"))
if a in l:
    print("found")
elif a not in l:
    print("not found")
'''


l=[1,3,4,5,6.6,"hello","t"]
a=int(input("Enter your search :"))
flag=1
for i in range(len(l)):
    if l[i]==a:
        pos=i
        flag=1
        break
if flag==1:
    print("element found at ",pos)
else:
    print("not found")