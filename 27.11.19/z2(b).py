from random import *
a=[]
k=randint(1,10)
print(k)
sp=[[randint(-100,100)for j in range(10)]for i in range(10)]
#for i in range(10):
#    for j in range(10):
#        print(sp[i][j],end=' ')
#    print()
for i in range(0,10):
    a.append(sp[k][i])
#print(a)
print(sum(a))
