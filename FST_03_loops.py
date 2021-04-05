#while loop
# intialiazation
# condition
# inc/dec

'''
i=0
while(i<5):
    print("hello world.")
    i=i+1
'''

#calculator using while loop
again=input("want to use calculator?(Y/N): ")
while(again=="Y"):
    a=int(input("Enter the no 1: "))
    b=int(input("Enter the no 2: "))
    print("1.Addition 2.Subtraction 3.Multiplication 4.Dividision")
    ch=int(input("Enter your choice: "))
    if(ch==1):
      print(a+b)
    elif(ch==2):
      print(a-b)
    elif(ch==3):
      print(a*b)
    elif(ch==4 and b!=0):
      #here we may get zero division error if second input is 0
      if(b==0):
        print("can't divide by zero")
      else:
        print(a/b)
    else:
        print(".....invalid choice.....")
  
    again=input("want to use calculator?(Y/N): ")

print("---We will meet you soon---")

