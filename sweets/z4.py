with open('input.txt', 'r') as f:
    a,b,c = map(int,f.readlines())
#print(a,b,c)
with open('output.txt','w') as f:
    if ((a-b)%3) == 0:
        f.write('3')
    elif ((a-c)%3) == 0:
        f.write('2')
    else:
        f.write('1')

    
