from random import *
#1 Juku läheb kinno
nimi=input("Mis on sinu nimi?").capitalize()
print("Tere ",nimi) #Tere, Anna"
if nimi=="Juku":
    print("Lähme kinno")
    vanus=int(input("Kui vana sa oled?"))
    if vanus<0 or vanus>100:
        pilet="vale vanus"
    elif vanus<6:
        pilet="tasuta pilet"
    elif vanus<=14:
        pilet="lastepilet"
    elif vanus<=65:
        pilet="täispilet"
    elif vanus<=100:
        pilet="sooduspilet"
    print(pilet) ##ilus ja õige vastus! "vale vastus" või "on vaja osta...."
else:
    print("Ma ootan Jukkut")
    
#2
nimi1 = input("Sisesta esimese inimese nimi: ")
nimi2 = input("Sisesta teise inimese nimi: ")
print("Täna on",nimi1, "ja" ,nimi2, "pinginaabrid!")

#3
pikkus = float(input("Sisesta seina pikkus meetrites: "))
laius = float(input("Sisesta teise seina pikkus meetrites: "))
pindala = pikkus * laius
print("Põranda pindala on" ,pindala, "ruutmeetrit.")
soov = input("Kas soovid remonti teha? (jah/ei): ")
if soov.lower() == "jah":
    
    hind = float(input("Sisesta ruutmeetri hind: "))
    
    remondi_hind = pindala * hind
    print("Remondi hind on" ,remondi_hind, "eurot.")
    

#4
alghind = float(input("Sisesta alghind: "))
soodushind = alghind * 0.7 if alghind > 700 else alghind
print("30% soodustusega hind on" ,soodushind, "eurot.")

#5
temperatuur = float(input("Sisesta temperatuur: "))
if temperatuur > 18:
    print("Temperatuur on üle 18 kraadi, soovitav toasoojus talvel.")
else:
    print("Temperatuur on 18 kraadi või madalam.")
    
#6
# Küsi inimese pikkus
pikkus = float(input("Sisesta inimese pikkus meetrites: "))

# Teata, kas ta on lühike, keskmine või pikk
if pikkus < 1.6:
    print("Inimene on lühike.")
elif 1.6 <= pikkus < 1.8:
    print("Inimene on keskmise pikkusega.")
else:
    print("Inimene on pikk.")
    

#7
# Küsi inimese pikkus ja sugu
pikkus = float(input("Sisesta inimese pikkus meetrites: "))
sugu = input("Sisesta inimese sugu (m/n): ")

# Teata, kas ta on lühike, keskmine või pikk
if sugu.lower() == "m":
    if pikkus < 1.6:
        print("Inimene on lühike mees.")
    elif 1.6 <= pikkus < 1.8:
        print("Inimene on keskmise pikkusega mees.")
    else:
        print("Inimene on pikk mees.")
elif sugu.lower() == "n":
    if pikkus < 1.6:
        print("Inimene on lühike naine.")
    elif 1.6 <= pikkus < 1.8:
        print("Inimene on keskmise pikkusega naine.")
    else:
        print("Inimene on pikk naine.")
else:
    print("Vale sugu.")



#8 
from datetime import *
arve_nr= date.today()#datetime.now()
print(arve_nr)
tsekk="Arve:  "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
summa=0

for toode in ["Piim", "Leib", "Komm"]:
    hind=randint(50,150)/100
    v=input("Toode:"+toode+"Hind"+str(hind)+"\nKas tahad osta?").lower()
    if v=="jah":
        mitu=int(input("mitu?"))
        tsekk+=toode+"  "+str(hind)+"   "+str(mitu)+"   "+str(mitu+hind)+"\n"
        summa+=mitu+hind
tsekk+="Kokku maksta: "+str(summa)
print(tsekk)
while True:
    raha=float(input("Maksa "+str(summa)+"\n"))
    if raha==summa:
        print("tänan ostu eest!")
        break 
    elif raha>summa:
        print("Tänan ostu eest! Tagasi "+str(raha-summa))
        break
    else:
        summa-=raha
        print("Maksa veel" +str(summa))



toode="Piim"
hind=randint(50,150)/100
v=input("Toode:"+toode+"Hind"+str(hind)+"\nKas tahad osta?").lower()
if v=="jah":
    mitu=int(input("mitu?"))
    tsekk+=toode+"  "+str(hind)+"   "+str(mitu)+"   "+str(mitu+hind)+"\n"
    summa+=mitu+hind
toode="leib"
hind=randint(90,300)/100
v=input("Toode:"+toode+"Hind:"+str(hind)+"\nKas tahad osta?").lower()
if v=="jah":
    mitu=int(input("mitu?"))
    tsekk+=toode+"  "+str(hind)+"   "+str(mitu)+"   "+str(mitu+hind)+"\n"
    summa+=mitu+hind
toode="Kommid"
hind=randint(600,1500)/100
v=input("Toode:"+toode+"Hind:"+str(hind)+"\nKas tahad osta?").lower()
if v=="jah":
    mitu=int(input("mitu?"))
    tsekk+=toode+"  "+str(hind)+"   "+str(mitu)+"   "+str(mitu+hind)+"\n"
    summa+=mitu+hind
    toode="leib"
tsekk+="Kokku maksta: "+str(summa)
print(tsekk)
raha=float(input("Maksa "+str(summa)))
