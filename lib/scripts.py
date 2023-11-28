#Plik przechowujący funkcję sprawdzające link i tworzące pliki bazy danych
import lib.scraper as scraper
import time

def sprawdz_baze_danych(tytul):
    nazwa_pliku = "Database/" + tytul + ".csv"
    try:
        plik = open(nazwa_pliku, "r")
        plik.close()
    except FileNotFoundError:
        return False

    return True

def sprawdz_sklep(adres):
    if(adres.find("euro.com.pl") != -1):
        return "RTV EURO AGD"
    elif(adres.find("komputronik.pl") != -1):
        return "Komputronik"
    elif(adres.find("x-kom.pl") != -1):
        return "x-kom"
    else:
        return None

def stworz_plik_bazy_danych(tytul):
    nazwa_pliku = "Database/" + tytul + ".csv"
    plik = open(nazwa_pliku, "w")
    plik.write(time.strftime("%d/%m %H:%M") + "\n")
    plik.close()

    return plik

def update_pliku_bazy_danych(tytul, sklep, cena):
    nazwa_pliku = "Database/" + tytul + ".csv"
    plik = open(nazwa_pliku, "a")
    plik.write(str(sklep) + "," + str(cena) + "\n")
    plik.close()

    return plik

def update_starego_pliku_bazy_danych( tytul):
    nazwa_pliku = "Database/" + tytul + ".csv"
    plik = open(nazwa_pliku, "a")
    plik.write("\n")
    plik.write(time.strftime("%d/%m %H:%M") + "\n")
    plik.close()

    return plik

def wczytaj_plik(nazwa_pliku_wejsciowego):
    plik = open(nazwa_pliku_wejsciowego, "r")
    adresy = plik.readlines()
    plik.close()

    return adresy