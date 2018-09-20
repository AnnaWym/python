def hotel_cost(nights):
    return 140 * nights


def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475


def rental_car_cost(days):
    cenaauta = days * 40
    if days >= 7:
        cenaauta = cenaauta - 50
    elif days >= 3:
        cenaauta = cenaauta - 20
    return cenaauta


def trip_cost(city, days, spending_money):
    kosztwycieczki = hotel_cost(days - 1) + plane_ride_cost(city) + rental_car_cost(days) + spending_money
    return kosztwycieczki

city = input("Podaj miasto: ")
dni = input("Podaj liczbę dni: ")
kieszonkowe = input("Podaj ilość kieszonkowego: ")

koszt = trip_cost(city, int(dni), int(kieszonkowe))

print (koszt)