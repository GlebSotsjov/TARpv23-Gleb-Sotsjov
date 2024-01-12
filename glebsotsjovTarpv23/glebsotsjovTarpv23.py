from random import *

aeg = float(input("Mitu tundi kulus sõiduks? ")) #aeg ei saa olla 0
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus/aeg
print("Sinu kiirus oli " + str(kiirus) + "km/h")
try:
    pass
except :
    pass
print("Tere maailm!")
1
nimi = input("Mis on sinu nimi?")
vanus=int(input("kui vana sa oled?"))
print("Tere tulemast!"  ,nimi, "Sa oled",vanus,"aastat vana")
print("Tere tulemast! {0} sa oled {1} aastat vana".format(nimi,vanus))
print("Muutuja vanus=",vanus,"tüüp on",type(vanus))
2
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True
print(type(vanus))
print(type(eesnimi))
print(type(pikkus))
print(type(kas_käib_koolis))
3
from random import *

kokku=randint(10,100)
print("kokku: ",kokku)
mitu = int(input("mitu kommi  tahad ära võtta?"))
kokku-=mitu
print("Nüüd Laua peal on",kokku,"kommid")
4
ümbermõõt = float(input("kirjutage puu umbermõõt: "))
diameeter = ümbermõõt / 3.14159
print("Puu diameeter:", diameeter)
5
N = float(input("Sisestage ristküliku pikkus N meetrites: "))
M = float(input("Sisestage ristküliku laius M meetrites: "))
diagonaali_pikkus = (N ** 2 + M ** 2) ** 0.5
print("Ristküliku diagonaali pikkus on:", diagonaali_pikkus , "meetrit")
6
# kiirus = teepikkus / aeg
7
number = [int(input("Sisestage Numbrit: ")) for _ in range(5)]
average = sum(number) / 5
print("The average is:", average)
# 8   @..@
#  (----)
#  ( \__/ )
# ^^ "" ^^
9
a=float(input("Sisestage numbrit: "))
b = float(input("Sisestage numbrit: "))
c = float(input("Sisestage numbrit: "))
P = a + b + c
print(P)
10
hinnang = 12.90
jootraha_protsent = 10
kokku = hinnang + (hinnang * (jootraha_protsent / 100))
igaüks_makseb = kokku / 2
print("Igaüks peab maksma:", igaüks_makseb, "eurot")