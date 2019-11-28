from random import *
a=[]
kurs=randint(1,5)
print('Взяли'+' '+str(kurs)+' '+'курс')
sp=[[randint(20,50)for j in range(8)]for i in range(5)]
for i in range(5):
    for j in range(8):
        print(sp[i][j],end=' ')
    print()
for i in range(0,8):
    a.append(sp[kurs-1][i])
print(a)
summ=sum(a)
print('Общее число студентов на'+' '+str(kurs)+' '+'курсе'+' '+'-'+' '+str(summ))
