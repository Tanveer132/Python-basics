#----student data using dictionary----

student={"Tanveer":100,"Kiran":99,"Akshay":101,"joy":80}

#max marks
high=0
for i in student.keys():
    if high<student[i]:
        high=student[i]
print(high)

#max marks with name of the student
high=0
topper=""
for i in student.keys():
    if high<student[i]:
        high=student[i]
        topper=i
print(high,topper)

for k,v in student.items():
    if high<v:
        high=v
        topper=k
print(high,topper)

#min marks 
low=student["Tanveer"]
for i in student.keys():
    if low>=student[i]:
        low=student[i]
print(low)


#max marks with name of the student
low=student["Tanveer"]
lower=""
for i in student.keys():
    if low>=student[i]:
        low=student[i]
        lower=i
print(low,lower)