#tuple
'''
t=1,3,4,5,6
#nesting tuple
t2=(1,3,4,5,6.6,"hello",t)
#accessing nesting tuple
print(t2[6][2])
print(t)
print(type(t))
#accessing the elements in the tuple
for i in range(5):
    print(t[i])
'''
'''
t2=(1,3,4,5,6.6,"hello",(67,45,23,(34,43,56,)),(54,67,54))

print(t2[6][0])  #access 67
print(t2[6][1])  #access 45
print(t2[6][3][0])  #accessing 34
print(t2[7][1])  #accessing 67
print(t2[5][0])  #access h
'''

#slicing in tuples
t=(1,2,3,4,55,6,7,8,9,10)
# print(t[:])
# print(t[0:9:2])
# print(t[1::2])
# print(t[8::-2])
# print(t[9:0:-2])
# tuple is a sequence which can be used in for loop
for i in t:
    print(i)

for i in range(len(t)):
    print(i,"=>",t[i])

