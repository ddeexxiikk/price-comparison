#Główny plik skryptu, wywołujący funkcje z pozostałych plików
import lib.scraper as scraper
import lib.scripts as scripts
import time

#Główna funkcja main, wywołująca pozostałe funkcje
def main():
    print("Witaj w Porównywarce cen!")
    print("Podaj tytuł produktu: ")
    tytul = input()

    adresy = []
    print("Podaj adres URL produktu: ")
    adresy.append(input())

    while(True):
        print("Czy chcesz podać kolejny adres? (y/n)")
        odp = input()
        if(odp == "y"):
            print("Podaj adres URL produktu: ")
            adresy.append(input())
        elif(odp == "n"):
            break
        else:
            print("Nieprawidłowa odpowiedź")
    print("Pobieram ceny dla Ciebie...")

    #Uruchomienie skryptów i stworzenie/update bazy danych
    licznik=0
    if(scripts.sprawdz_baze_danych(tytul) == True):
        scripts.update_starego_pliku_bazy_danych(tytul)

        for adres in adresy:
            sklep = scripts.sprawdz_sklep(adres)
            if(sklep == None):
                licznik += 1
                continue
            elif(sklep == "RTV EURO AGD"):
                rtv_euro_agd = scraper.pobierz_dane_RTV_EURO_AGD(adres)
                scripts.update_pliku_bazy_danych(tytul, "RTV EURO AGD", rtv_euro_agd)
            elif(sklep == "Komputronik"):
                komputronik = scraper.pobierz_dane_Komputronik(adres)
                scripts.update_pliku_bazy_danych(tytul, "Komputronik", komputronik)
            elif(sklep == "x-kom"):
                x_kom = scraper.pobierz_dane_X_Kom(adres)
                scripts.update_pliku_bazy_danych(tytul, "x-kom", x_kom)
    else:
        scripts.stworz_plik_bazy_danych(tytul)
        for adres in adresy:
            sklep = scripts.sprawdz_sklep(adres)
            if(sklep == None):
                licznik += 1
                continue
            elif(sklep == "RTV EURO AGD"):
                rtv_euro_agd = scraper.pobierz_dane_RTV_EURO_AGD(adres)
                scripts.update_pliku_bazy_danych(tytul, "RTV EURO AGD", rtv_euro_agd)
            elif(sklep == "Komputronik"):
                komputronik = scraper.pobierz_dane_Komputronik(adres)
                scripts.update_pliku_bazy_danych(tytul, "Komputronik", komputronik)
            elif(sklep == "x-kom"):
                x_kom = scraper.pobierz_dane_X_Kom(adres)
                scripts.update_pliku_bazy_danych(tytul, "x-kom", x_kom)
        
    #Jeśli licznik jest równy długości listy adresów, to znaczy, że nie udało się pobrać danych z żadnego sklepu
    if(licznik == len(adresy)):
        print("Nie udało się pobrać danych z żadnego sklepu")
        time.sleep(2)
        print("Wciśnij dowolny klawisz, aby zamknąć okno")
        input()
        exit()

    #Zakończenie skryptu
    print("Porównanie cen czeka na Ciebie w pliku. Miłego Dnia!")
    time.sleep(2)
    print("Wciśnij dowolny klawisz, aby zamknąć okno")
    input()
    

#Wywołanie funkcji main
if __name__ == "__main__":
    main()