from math import sqrt
import datetime

def WypiszWiek():
    print ("29")

def WypiszImie():
    print ("Ania")

def CzyLiczbaParzysta(liczba):
    wynik = liczba % 2
    if wynik == 0:
        print ("liczba parzysta")
    else:
        print ("liczba nieparzysta")

def SprawdzWynikDzielenia(liczba):
    wynik3 = liczba % 3
    wynik5 = liczba % 5
    if wynik3 == 0 and wynik5 == 0:
        print ("liczba podzielna przez 3 i 5")
    else:
        print ("liczba niepodzielna przez 3 i 5")

def PodniesDoPotegiTrzeciej(liczba):
    potega = liczba ** 3
    print (potega)

def WypiszPierwiastek(liczba):
    pierwiastek = sqrt(liczba)
    print (pierwiastek)

def WykonajDzialania(liczba1, liczba2):
    roznica = liczba1 - liczba2
    iloczyn = liczba1 * liczba2
    suma = liczba1 + liczba2
    print (f"suma = {suma}, iloczyn = {iloczyn}, różnica = {roznica} ")

def WypiszDate():
    data = datetime.datetime.now()
    print (data)

def WypiszLitery(slowo, ilosc):
    nowe_slowo = slowo[:ilosc]
    print (nowe_slowo)

def WypiszLitere(slowo, numerLitery):
    nowe_slowo = slowo[numerLitery]
    print (nowe_slowo)


WypiszImie()
WypiszWiek()
WypiszLitere("Ania", 1)
WypiszLitery("Ariel", 3)
WypiszDate()
WykonajDzialania(5, 2)
WypiszPierwiastek(4)
PodniesDoPotegiTrzeciej(2)
SprawdzWynikDzielenia(15)
SprawdzWynikDzielenia(16)
CzyLiczbaParzysta(2)
CzyLiczbaParzysta(7)
