#Plik zawiera funkcje do pobierania danych z podanych stron internetowych
import requests
from bs4 import BeautifulSoup

def pobierz_dane_RTV_EURO_AGD(adres):
    page = requests.get(adres)

    if(page.status_code != 200):
        print("Błąd połączenia z serwerem")
        return None
    
    soup = BeautifulSoup(page.content, 'html.parser')
    get_price = soup.find(class_="price-template__large--total").get_text()

    return get_price

def pobierz_dane_Komputronik(adres):
    page = requests.get(adres)

    if(page.status_code != 200):
        print("Błąd połączenia z serwerem")
        return None
    
    soup = BeautifulSoup(page.content, 'html.parser')
    get_price = soup.find(class_="font-bold leading-8 text-3xl").get_text()

    return get_price

'''
def pobierz_dane_Media_Markt(adres):
    page = requests.get(adres)

    if(page.status_code != 200):
        print("Błąd połączenia z serwerem")
        return None
    
    soup = BeautifulSoup(page.content, 'html.parser')
    get_price = soup.find(class_=" ").get_text()
    
    return get_price

def pobierz_dane_Neonet(adres):
    page = requests.get(adres)

    if(page.status_code != 200):
        print("Błąd połączenia z serwerem")
        return None
    
    soup = BeautifulSoup(page.content, 'html.parser')
    get_price = soup.find(class_="uiPriceScss-integer-38D")
    print(get_price)

    return get_price

def pobierz_dane_X_Kom(adres):
    page = requests.get(adres)

    if(page.status_code != 200):
        print("Błąd połączenia z serwerem")
        return None
    
    soup = BeautifulSoup(page.content, 'html.parser')
    get_price = soup.find(class_="sc-n4n86h-1 hYfBFq").get_text()
    print(get_price)

    return get_price

def pobierz_dane_Media_Expert(adres):
    page = requests.get(adres)

    if(page.status_code != 200):
        print("Błąd połączenia z serwerem")
        return None
    
    soup = BeautifulSoup(page.content, 'html.parser')
    get_price = soup.find(class_="whole").get_text()

    return get_price


def pobierz_dane_Avans(adres):
    page = requests.get(adres)

    if(page.status_code != 200):
        print("Błąd połączenia z serwerem")
        return None
    
    soup = BeautifulSoup(page.content, 'html.parser')
    get_price = soup.find(class_="a-price_price").get_text()

    return get_price

def pobierz_dane_Allegro(adres):
    page = requests.get(adres)

    if(page.status_code != 200):
        print("Błąd połączenia z serwerem")
        return None
    
    soup = BeautifulSoup(page.content, 'html.parser')
    get_price = soup.find(class_="aria-hidden").get_text()   

    return get_price
'''    