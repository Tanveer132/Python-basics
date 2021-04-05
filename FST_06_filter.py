#filter function

def check(a):
    if a%2==0:
        return True
    else:
        return False
res=list(filter(lambda a:a%2==0, [1,2,3,4,5,6,7,8]))
print(res)

res=list(filter(check, [1,2,3,4,5,6,7,8]))
print(res)