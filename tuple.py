# y="a",
# print(y,type(y)) #('a' ,) tuple
# h=(3,6.8,'by',None)
# print(type(h))#tuple
# print(h[0])#3
# h[0]=5 #TypeError:tuple object does not support itrm assignment
# c=print('hi')#hi
# d=print(c)#None
# print(c,type(c))#None NoneType
# x=(1)
# print(x,type(x))#1 int
# x=(1,)
# print(x,type(x))#(1,) tuple
# pr=('apple','realme','vivo','samsung')
# pr[1]="nokia" #TypeError:tuple object does not support itrm assignment
# m="Hello" , "World"
# print(m,type(m))#('Hello', 'World') tuple
# print(m[2])#IndexError: tuple index out of range
# v=(1,4.2,'hello',[2,3],('H','D'),None,True)
# print(v,type(v))#=(1,4.2,'hello',[2,3],('H','D'),None,True) tuple
# v=(1,4.2,'hello',[2,3],('H','D'))
# v[0]=21 #TypeError:tuple object does not support itrm assignment
# x=(1,4.2,'hello',[2,3],('H','D'))
# print(x.count(4.2)) #1
# print(x.index(24.7)) #ValueError:24.7 is not in tuple
# print(dir(tuple)) #('count','index')