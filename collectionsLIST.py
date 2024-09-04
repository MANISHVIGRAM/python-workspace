print("LIST")
print("*Allows duplicates")
print("We can store any datatypes")
print("We can modify- add or remove")
print("list functions - insert,append,extend,pop")
a=[1,2,3,4,5]
print(type(a))
print(a)
a.append(6)
print(a)
a.insert(3,33)
a[0]=11
print(a)
a.pop(5)
print(a)
b=[22,44,66]
a.extend(b)
print(a)