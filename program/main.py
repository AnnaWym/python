# nowy program
imie = input("podaj imię: ")
wiek = input("ile masz lat?: ")
plec = input("podaj płeć K lub M: ")

def WypiszDane(imie, wiek, nazwa_plci):
    print (f"masz na imię: {imie}, masz {wiek} lat i jesteś {nazwa_plci}")

if plec == "K":
    WypiszDane(imie, wiek, "kobietą")

elif plec == "M":
    WypiszDane(imie, wiek, "mężczyzną")

else:
    print ("błędny symbol płci")
