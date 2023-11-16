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

    #Zakończenie skryptu
    print("Porównanie cen czeka na Ciebie w pliku. Miłego Dnia!")
    time.sleep(3)
    print("Wciśnij dowolny klawisz, aby zamknąć okno")
    input()
    

#Wywołanie funkcji main
if __name__ == "__main__":
    main()