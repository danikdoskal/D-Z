from tkinter import *

root=Tk()
root.title('Численность популяций')
root.geometry('550x530')

def neogr(event):
    a=float(txt_a.get())
    N=int(txt_cikl.get())
    zhertv=int(txt_2zh.get())

    for i in range(N):
        zhertv=zhertv*a

    lb_1['text']=str(int(zhertv))

def ogr(event):
    a=float(txt_a.get())
    b=float(txt_b.get())
    N=int(txt_cikl.get())
    zhertv=int(txt_2zh.get())

    for i in range(N):
        zhertv=zhertv*(a-b*zhertv)

    lb_2['text']=str(int(zhertv))    

def ogr_w_otl(event):
    a=float(txt_a.get())
    b=float(txt_b.get())
    c=float(txt_c.get())
    N=int(txt_cikl.get())
    zhertv=int(txt_2zh.get())

    for i in range(N):
        zhertv=(a-b*zhertv)*zhertv-c

    lb_3['text']=str(int(zhertv))    

def zher_xi(event):
    a=float(txt_a.get())
    b=float(txt_b.get())
    c=float(txt_c.get())
    f=float(txt_f.get())
    g=float(txt_g.get())
    d=float(txt_d.get())
    N=int(txt_cikl.get())
    zhertv=int(txt_2zh.get())
    xi=int(txt_2xi.get())

    for i in range(N):
        zhertv=(a-b*zhertv)*zhertv-c-f*zhertv*xi
        xi=d*xi+g*zhertv*xi

    lb_42['text']=str(int(zhertv))
    lb_123['text']=str(int(xi))


lb_rost=Label(root, text='Неограниченный рост', bg='gray', width=70,heigh=1); lb_rost.place(x=40,y=10)
lb_a=Label(root, text='a',bg='orange',width=3,height=1);lb_a.place(x=5, y=40)
txt_a=Entry(root,width=5,bg='white', );txt_a.place(x=40, y=40)
but_rost=Button(root,text='Неограниченный рост', width=25, height=1, bg='orange');but_rost.place(x=80,y=40);but_rost.bind('<Button-1>',neogr)
lb_1=Label(root,bg='white', width=25);lb_1.place(x=275,y=40)

lb_ogr=Label(root, text='Ограниченный рост', bg='gray', width=70,heigh=1); lb_ogr.place(x=40,y=70)
lb_b=Label(root, text='b',bg='red',width=3,height=1);lb_b.place(x=5, y=100)
txt_b=Entry(root,width=5,bg='white' );txt_b.place(x=40, y=100)
but_ogr=Button(root,text='Ограниченный рост', width=25, height=1, bg='red');but_ogr.place(x=80,y=100);but_ogr.bind('<Button-1>',ogr)
lb_2=Label(root,bg='white', width=10);lb_2.place(x=275,y=100)

lb_sotl=Label(root, text='Ограниченный рост с отловом', bg='gray', width=70,heigh=1); lb_sotl.place(x=40,y=130)
lb_c=Label(root, text='c',bg='yellow',width=3,height=1);lb_c.place(x=5, y=160)
txt_c=Entry(root,width=5,bg='white' );txt_c.place(x=40, y=160)
but_sotl=Button(root,text='Ограниченный рост с отловом', width=25, height=1, bg='yellow');but_sotl.place(x=80,y=160);but_sotl.bind('<Button-1>',ogr_w_otl)
lb_3=Label(root,bg='white', width=10);lb_3.place(x=275,y=160)

lb_zhertva=Label(root, text='Жертва-хищник', bg='gray', width=70,heigh=1); lb_zhertva.place(x=40,y=190)
lb_d=Label(root, text='d',bg='silver',width=3,height=1);lb_d.place(x=5, y=220)
txt_d=Entry(root,width=5,bg='white');txt_d.place(x=40,y=220)
lb_f=Label(root, text='f',bg='silver',width=3,height=1);lb_f.place(x=80, y=220)
txt_f=Entry(root,width=5,bg='white');txt_f.place(x=115,y=220)
lb_g=Label(root, text='g',bg='silver',width=3,height=1);lb_g.place(x=155, y=220)
txt_g=Entry(root,width=5,bg='white');txt_g.place(x=190,y=220)
but_zhertva=Button(root,text='Жертва-хищник', width=20, height=1,bg='gold');but_zhertva.place(x=270,y=220);but_zhertva.bind('<Button-1>',zher_xi)

lb_colzher=Label(root, text='Жертвы',bg='gray',width=10,height=1);lb_colzher.place(x=60, y=250)
lb_42=Label(root, bg='white',width=5,height=1);lb_42.place(x=140, y=250)
lb_colxi=Label(root, text='Хищники',bg='gray',width=10,height=1);lb_colxi.place(x=300, y=250)
lb_123=Label(root,bg='white',width=5,height=1);lb_123.place(x=380, y=250)

lb_2zh=Label(root, text='Жертвы',bg='red',width=10,height=1);lb_2zh.place(x=2, y=290)
txt_2zh=Entry(root,width=5,bg='white');txt_2zh.place(x=130,y=290)

lb_2xi=Label(root, text='Хищники',bg='orange',width=10,height=1);lb_2xi.place(x=2, y=320)
txt_2xi=Entry(root,width=5,bg='white');txt_2xi.place(x=130,y=320)

lb_cikl=Label(root, text='Кол. циклов',bg='yellow',width=15,height=1);lb_cikl.place(x=2, y=360)
txt_cikl=Entry(root,width=5,bg='white');txt_cikl.place(x=130,y=360)

but_grafic=Button(root,text='График', width=10, height=1,bg='coral');but_grafic.place(x=60,y=400)


    
root.mainloop()
