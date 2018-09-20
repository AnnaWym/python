miesiac = input("Podaj miesiąc urodzin: ")
dzien = input("Podaj dzień urodzin: ")

if miesiac == "styczeń" and int(dzien) <= 19:
    print ("Twój znak zodiaku to: Koziorożec")

elif miesiac == "grudzień" and int(dzien) >= 22:
    print ("Twój znak zodiaku to: Koziorożec")

elif miesiac == "styczeń" and int(dzien) >= 20:
    print ("Twój znak zodiaku to: Wodnik")

elif miesiac == "luty" and int(dzien) <= 18:
    print ("Twój znak zodiaku to: Wodnik")

elif miesiac == "luty" and int(dzien) >= 19:
    print ("Twój znak zodiaku to: Ryby")

elif miesiac == "marzec" and int(dzien) <= 20:
    print ("Twój znak zodiaku to: Ryby")

elif miesiac == "marzec" and int(dzien) >= 21:
    print ("Twój znak zodiaku to: Baran")

elif miesiac == "kwiecień" and int(dzien) <= 19:
    print ("Twój znak zodiaku to: Baran")

elif miesiac == "kwiecień" and int(dzien) >= 20:
    print ("Twój znak zodiaku to: Byk")

elif miesiac == "maj" and int(dzien) <= 22:
    print ("Twój znak zodiaku to: Byk")

elif miesiac == "maj" and int(dzien) >= 23:
    print ("Twój znak zodiaku to: Bliźnięta")

elif miesiac == "czerwiec" and int(dzien) <= 21:
    print ("Twój znak zodiaku to: Bliźnięta")

elif miesiac == "czerwiec" and int(dzien) >= 22:
    print ("Twój znak zodiaku to: Rak")

elif miesiac == "lipiec" and int(dzien) <= 22:
    print ("Twój znak zodiaku to: Rak")

elif miesiac == "lipiec" and int(dzien) >= 23:
    print ("Twój znak zodiaku to: Lew")

elif miesiac == "sierpień" and int(dzien) <= 23:
    print ("Twój znak zodiaku to: Lew")

elif miesiac == "sierpień" and int(dzien) >= 24:
    print ("Twój znak zodiaku to: Panna")

elif miesiac == "wrzesień" and int(dzien) <= 22:
    print ("Twój znak zodiaku to: Panna")

elif miesiac == "wrzesień" and int(dzien) >= 23:
    print ("Twój znak zodiaku to: Waga")

elif miesiac == "październik" and int(dzien) <= 22:
    print ("Twój znak zodiaku to: Waga")

elif miesiac == "październik" and int(dzien) >= 23:
    print ("Twój znak zodiaku to: Skorpion")

elif miesiac == "listopad" and int(dzien) <= 21:
    print ("Twój znak zodiaku to: Skorpion")

elif miesiac == "listopad" and int(dzien) >= 22:
    print ("Twój znak zodiaku to: Strzelec")

else:
    print("Twój znak zodiaku to: Strzelec")
