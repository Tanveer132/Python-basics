#LIST

# l=[1,3,4,5,6]
# #nesting list
# l2=[1,3,4,5,6.6,"hello",t]
# #accessing nesting list
# print(t2[6][2])



# #list operations
# # 1. list.append(value)
# l=["milk","eggs","sugar","Oil"]
# l.append(7)
# print(l)

# #2. list.remove(value)
# l.remove(7)
# print(l)

# #3. list.pop(value)
# item=l.pop()
# print(l)
# print(item)

# #4. list.insert(index,value)
# l.insert(2,"ice-cream")
# print(l)


# for i in l:
#     print(i)

# for i in range(len(l)):
#     print(i,"=>",l[i])



# n=int(input("Enter the number of students: "))
# student=[]
# for i in range(n):
#     name=input("Enter the name of the student: ")
#     student.append(name)
# print(student)


n=int(input("Enter the number of students: "))
student=[]
for i in range(n):
    name=input("Enter the name of the student :")
    marks=int(input("Enter the marks :"))
    student.append([name,marks])
print(student)
    