from random import*
sp=[[randint(-100,100)for j in range(10)]for i in range(10)]
a=[]
st=int(input('Введите номер строки'))
for i in range(10):
    for j in range(10):
        print(sp[i][j],end=' ')
    print()
for i in range(0,8):
    a.append(sp[st-1][i])
print(a)
print(min(a))
