# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:56:22 2020

@author: Денис
"""
from time import sleep
def progress(percent=0, width=30):
    left = width * percent // 100
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']', f' {percent:.0f}%', sep='', end='', flush=True)
for i in range(101):
    progress(i)
    sleep(0.1)
    
    
def myfunc(n):
    return lambda a: a * n
mydoubler = myfunc(2)
print(mydoubler(11))


def myfunc(n):
    return lambda a: a * n
mytripler = myfunc(3)
print(mytripler(11))






import winsound as ws
import time as tm

def Morze(word):
    morze={'a':'.-',
           'б':'-...',
           'в':'·--',
           'г':'--.',
           'д':'-..',
           'е':'.',
           'ж':'...-',
           'з':'--..',
           'и':'..',
           'й':'.---',
           'к':'-.-',
           'л':'.-..',
           'м':'--',
           'н':'-.',
           'о':'---',
           'п':'.--.',
           'р':'.-.',
           'с':'...',
           'т':'-',
           'у':'..-',
           'ф':'..-.',
           'х':'....',
           'ц':'-.-.',
           'ч':'---.',
           'ш':'----',
           'щ':'--.-',
           'ъ':'--.--',
           'ы':'-.--',
           'ь':'-..-',
           'э':'..-..',
           'ю':'..--',
           'я':'.-.-'}
    rezult=[]
    for elem in word:
        rezult.append(morze[elem])
    print (rezult)
    return rezult

frequency=1000
cont=Morze(input().lower())
for s in cont:
    for symvol in s:
        print (symvol)
        if symvol== '.':
            ws.Beep(frequency,400)
        elif symvol== '-':
            ws.Beep(frequency,700)
    tm.sleep(1)
         
