from cmath import pi, sqrt
import math
from xml.etree.ElementTree import PI            #не правильный порядок
print("Ruudu karakteristikud")
a=float(input('Sisesta ruudu külje pikkus => '))     #float
S=a**2
print("Ruudu pindala",round(S,2))
P=4 * a
print("Ruudu ümbermõõt",round (P,2))
di=a*sqrt(2)        #Sqrt
print("Ruudu diagonaal",di)
print()
print("Ristküliku karakteristikud")            #лишняя скопка
b=float(input("Sisesta ristküliku 1. külje pikkus => "))         #float
c=float(input("Sisesta ristküliku 2. külje pikkus => "))          #float
S=b*c
print("Ristküliku pindala", S)   # ""
P=2*(b+c)      #*
print("Ristküliku ümbermõõt", P)
di=sqrt(b**2 + c**2)       #math - + **
print("Ristküliku diagonaal"), (di)          #не закрытая скопка
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => " ))    #ковычки
d= 2 * r      #*
print("Ringi läbimõõt",str( d))         #ошибка в коде
S=pi*r**2
print("Ringi pindala", round(S,2))
C=2*pi*r
print("Ringjoone pikkus", round(C,2))           #не закрыта скопка
