#Plik przechowujący funkcję sprawdzające link i tworzące pliki bazy danych
import scraper
import time


def sprawdz_sklep(adres):
    if(adres.find("euro.com.pl") != -1):
        return "RTV EURO AGD"
    elif(adres.find("komputronik.pl") != -1):
        return "Komputronik"
    else:
        return None
    
    '''
    elif(adres.find("mediamarkt.pl") != -1):
        return "Media Markt"
    elif(adres.find("neonet.pl") != -1):
        return "Neonet"
    elif(adres.find("x-kom.pl") != -1):
        return "x-kom"
    elif(adres.find("mediaexpert.pl") != -1):
        return "Media Expert"
    elif(adres.find("avans.pl") != -1):
        return "Avans"
    elif(adres.find("allegro.pl") != -1):
        return "Allegro"
    '''

def stworz_plik_bazy_danych(tytul):
    #Stworz plik CSV z tytulem i data w folderze Database
    nazwa_pliku = "Database/" + tytul + ".csv"
    plik = open(nazwa_pliku, "w")
    #Dodaj naglowki do pliku: w pierwszej linii data wraz z godziną, w drugiej sklep,cena 
    plik.write("Data: " + time.strftime("%d/%m %H:%M") + "\n")
    plik.write("Sklep,Cena\n")
    plik.close()

    return plik

def update_pliku_bazy_danych(tytul, sklep, cena):
    #Otworz plik CSV z tytulem w folderze Database
    nazwa_pliku = "Database/" + tytul + ".csv"
    plik = open(nazwa_pliku, "a")
    #Dodaj do pliku sklep i cene
    plik.write(sklep + "," + cena + "\n")
    plik.close()

    return plik