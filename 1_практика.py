# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:49:16 2020

@author: Денис
"""
print("Hello, world!")




a=None
b=6
c=5.4
d='7.9'
e=[b,4,6.6,d,'print']
f=(3,5,7,6.6)
g={a:a**2 for a in range(7)}
h={'a', 'b', 'c', 'd'}


print('a=',type(a))
print('b=',type(b))
print('c=',type(c))
print('d=',type(d))
print('e=',type(e))
print('f=',type(f))
print('g=',type(g))
print('h=',type(h))


b=float(b)
c=int(c)
print('b=',type(b))
print('c=',type(c))

b=str(b)
d=float(d)
print('b=',type(b))
print('d=',type(d))


print('b:',len(b))
print('e:',len(e))
print('f:',len(f))
print('g:',len(g))
print('h:',len(h))


print(b[0],b[-1])
print(e[0],e[-1])
print(f[0],f[-1])


print(b[1:-1])
print(e[1:-1])
print(f[1:-1])


print(g[2])




i=True
j=False
print('i=',type(i))
print('j=',type(j))


print(i and j)
print(i or j)
print(not(j))


k=5
l=3
print(k==l)
print(k!=l)
print(k>l)
print(k<l)
print(l>=k)
print(l<=k)


print(k+l)
print(k-l)
print(k*l)
print(k/l)
print(k**l)
print(k%l)
print(k//l)




print("Введите число от -100 до 100")
m= int(input())
if m<-100 and m>100:
    print("число не входит в диапазон [-100; 100]")
elif m<-50:
    print("число меньше -50")
elif m==-50:
    print("число равно -50")
elif m<0 and m>-50:
    print("число меньше 0, но больше -50")
elif m>0 and m<50:
    print ("число больше 0, но меньше 50")
elif m==50:
    print("число равно 50")
else:
    print("число больше 50")




for i in range(11):
    print(i, end=' ')


n=0
while n!=11:
    print(n)
    n=n+1


p="Панкратов Денис Андреевич"
for r in p:
    print(r, end=" ")
print()
    
r=["Егор","Михаил", "Ярослав"]
for o in r:
    print(o)


q={'Егор': '26.06.2000','Михаил': '15.04.1999', 'Ярослав': '05.10.2000'}
for key in q:
    if q[key][3:5]== '06' or q[key][3:5]== '07' or q[key][3:5]== '08':
        print(key, q[key])
        
    
    
    
def func():
    print('Hello world!')
    
func()


def name(s):
    print(s)
    
s="Денис"
name(s)


def nameage():
    print("Введите своё имя")
    name=input()
    print("Введите свой возраст")
    age=input()
    return name+" "+age

print(nameage())

def diskr(a,b,c):
    d=b*b-4*a*c
    return d

a=4
b=6
c=2
print(diskr(a,b,c))


def alf(a):
    if a>33 and a<1:
        print('Указано не правильное число!')
    else:
        a=a+1071
        print(chr(a))
        
alf(int(input()))
       
   



fi="Панкратов Денис"
ot=" Андреевич"
print(len(fi))
print(fi+ot)
print(fi[9:])
fio=fi+ot
print(fio.upper())
print(fio.split())




f=(3,5,7,6.6)
e=[b,4,6.6,d,'print']
g={a:a**2 for a in range(7)}
t=[None,5,6.2,'Денис',e,f,g]
for i, item in enumerate(t):
    print(i,type(item))

t.pop()

u=list(t[3])
print(u)

st=''
print(st.join(u))

for i, item in enumerate(st.join(u)):
    print(i,'-',item)
    
x=0    
for i in u:
    if i=='и':
        x=x+1
print(x)





numbers = []
for i in range(1, 101):
    if i % 2 != 0:
        numbers.append(i)
print(numbers)





def dell(a,b):
    try:
        rez=a/b
    except ZeroDivisionError:
        print("Делить на ноль нельзя")
    else:
        return rez
    
dell(int(input()),int(input()))