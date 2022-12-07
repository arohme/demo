#tuples are used to store multiple itemes in a single variable.
#a tuple is a collection which ordered and unchangeable

# tuple1=("apple","banana","cherry")
# print(tuple1)
# tuple1=list(tuple1)
# m=tuple1[0]="kiwi"
# m=tuple1
# print(m)
# m.append("mango")
# print(m)
# # m.clear()
# # print(m)
# m.copy()
# print(m)
# m.remove("kiwi")
# print(m)
# m.sort()
# print(m)
# m.append("ZAng")
# m.sort()
# print(m)
# m.sort(reverse=True)
# print(m)
# m=tuple(m)
# print(m)

# tip=(1,2,3,4,5)
# y=("a","b","c")
# x=tip+y # we cant add anything but we can join any thing.
# print(x)

# #unpacking a tuple
# tup=(3,4,5,6,7)
# a,b,c,d,e=tup # by using this you can unpack tuple
# print(a,b,c,d,e)

k=(3,4,5,6,7,8)
a,b,*c=k # if we are using * the tuple  make list of that things
print(a,b,c)
a,*b,c=k 
print(a,b,c)