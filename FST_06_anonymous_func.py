#create a lambda function to get square of the number

#function_name= lambda arg_name : function condition
x=lambda a : a**2
print(x(4))

#filter function

res=list(filter(lambda a:a%2==0, [1,2,3,4,5,6,7,8]))
print(res)