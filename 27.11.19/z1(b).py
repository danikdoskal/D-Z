from random import *
a=[]
s=randint(1,10)
print(s)
sp=[[randint(-100,100)for j in range(10)]for i in range(10)]
#for i in range(10):
#    for j in range(10):
#        print(sp[i][j],end=' ')
#    print()
for i in range(0,10):
    a.append(sp[i][s])
#print(a)
print(sum(a))
