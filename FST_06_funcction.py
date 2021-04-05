#understanding multiple arguments

# def scam(*arg):
#     print(arg[3])
#     print("hii")
#     print(arg)
#     print(type(arg))
#     print(arg[3])
#     for i in arg:
#         print(i)

# scam(2,3,4,5,6,7,8)

#-----keyword argument function
# def myfun(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     print(kwargs["name"])
#     print(kwargs["roll_no"])
#     print(kwargs["marks"])

# myfun(name="Tanveer", roll_no=0, marks=100)

#application

def minmax(lst):
    high=lst[0]
    low=lst[0]
    for i in lst:
        if i>high:
            high=i
    for i in lst:
        if i<low:
            low=i
    return low,high

def oddeven(lst):
    for i in lst:
        if i%2==0:
            print(i," is even")
        else:
            print(i," is odd")   
def palindrom(name):
    if name==name[: :-1]:
        print(name, " is palindrom")
    else:
        print(name," is not palindrom")
            

lst=(2,3,4,5,6)
minimum,maximum=minmax(lst)
print(minimum," is minimum and ",maximum," is maximum")
oddeven(lst)
name="nutan"
palindrom(name)


