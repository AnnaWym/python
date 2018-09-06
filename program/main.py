# nowy program
imie = input("podaj imię: ")
wiek = input("ile masz lat?: ")
plec = input("podaj płeć K lub M: ")
nazwa_plci = ""

if plec == "K":
    nazwa_plci = "kobietą"
    print (f"masz na imię: {imie}, masz {wiek} lat i jesteś {nazwa_plci}")

elif plec == "M":
    nazwa_plci = "mężczyzną"
    print(f"masz na imię: {imie}, masz {wiek} lat i jesteś {nazwa_plci}")

else:
    print ("błędny symbol płci")



