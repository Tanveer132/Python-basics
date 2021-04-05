#dictionary 
s={}
print(s)
print(type(s))

#set
s=set()
print(s)
print(type(s))

s={1,2,3,3,4,5,6}
print(s)
print(type(s))

#add element in set
s.add(6)
print(s)

#update mutliple elements in the set
s.update((9,8),[56,3,2],"sbc")
print(s)


#discard and remove
s.discard(6)
print(s)     #discards operation if element is unavailable in set
s.remove("s")
print(s)    #error occurs when tries to remove element which is not available in the set
