#-----FUNCTIONS WITH RETURN IN THE PYTHON------

# def add(a,b):
#     c=a+b
#     return a,b,c

# n1,n2,c=add(34,45)

# res=add(67,54)
# print(res)
# d=c+15
# print(n1,n2,d)

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        return "invalid argument"
    else:
        return a/b

def rem(a,b):
    return a%b

def divv(a,b):
    return a//b

ch=0
while(ch<6):
    n1=int(input("Enter the number 1 :"))
    n2=int(input("Enter the number 2 :"))
    ch=int(input('''--Enter your choice--
    1.Addition
    2.Subtraction
    3.Multiplication
    4.Division
    5.Remaiander
    6.Divvision
    =>'''))
    if ch==1:
        res=add(n1,n2)
        print(res)

    elif ch==2:
        res=sub(n1,n2)
        print(res)
        

    elif ch==3:
        res=mul(n1,n2)
        print(res)

    elif ch==4:
        res=div(n1,n2)
        print(res)

    elif ch==5:
        res=rem(n1,n2)
        print(res)

    elif ch==6:
        res=divv(n1,n2)
        print(res)

def hello():
    print("this function to be used in another file only")