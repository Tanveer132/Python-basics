#Enter the name of the students and their marks in PCM

#created the empty dictionary
stud={"Tanveer":[70,70,70], "Akshay":[80,80,80]}

n=0

while(n<4):
    #Ask user to get number of inputs
    print("\n___Enter your choice___")
    n=int(input('''    1.Display students data
    2.Add student data
    3.Get result
    ==>'''))
    #to print student data
    if n==1:
        print(stud)
        

    #to get new student in dictionary
    elif n==2:
        name=input("Enter the name of the student :")
        marks=[]
        for i in range(3):
            m=int(input("enter the marks of phy Chem Maths resp. :"))
            marks.append(m)
        print(marks)
        stud[name]=marks
        print(stud)
        
    
    #to get result of entered student in dictionary
    elif n==3:
        output={}
        print(stud)
        name=input("Enter the name of student :")
        total=0
        for k in stud[name]:
            total+=k
        #print(name, " => " ,total)
        output[name]=total
        print(output)

        if total>=150:
            print("....***Group cleared***....")
        else:
            print("....***FAIL***....")

        
        