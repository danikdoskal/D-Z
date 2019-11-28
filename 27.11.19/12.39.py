from random import *
a=[]
sp=[[randint(0,1)for j in range(36)]for i in range(25)]
#for i in range(25):
#    for j in range(36):
#        print(sp[i][j],end=' ')
#    print()
for i in range(0,36):
    a.append(sp[11][i])
#print(a)
print(sum(a))
