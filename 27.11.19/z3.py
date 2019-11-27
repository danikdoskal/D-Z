from random import *
a=[]
sp=[[randint(20,30)for j in range(10)]for i in range(10)]
#for i in range(10):
#    for j in range(10):
#        print(sp[i][j],end=' ')
#    print()
for i in range(0,10):
    a.append(sp[i][4])
#print(a)
print(sum(a))
