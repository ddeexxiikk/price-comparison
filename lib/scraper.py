#Plik zawiera funkcje do pobierania danych z podanych stron internetowych
import requests
from bs4 import BeautifulSoup

def pobierz_dane_RTV_EURO_AGD(adres):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    page = requests.get(adres, headers=headers)

    if(page.status_code != 200):
        return None
    
    soup = BeautifulSoup(page.content, 'html.parser')
    get_price = str(soup.find(class_="price-template__large--total").get_text())

    return get_price

def pobierz_dane_Komputronik(adres):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    page = requests.get(adres, headers=headers)

    if(page.status_code != 200):
        return None
    
    soup = BeautifulSoup(page.content, 'html.parser')
    get_price = str(soup.find(class_="font-bold leading-8 text-3xl").get_text())

    return get_price

def pobierz_dane_X_Kom(adres):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    page = requests.get(adres, headers=headers)

    if(page.status_code != 200):
        return None
    
    soup = BeautifulSoup(page.content, 'html.parser')
    get_price = str(soup.find(class_="sc-n4n86h-1 hYfBFq").get_text())

    return get_price

'''
def pobierz_dane_Media_Expert(adres):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    page = requests.get(adres, headers=headers)

    if(page.status_code != 200):
        print("Błąd połączenia z serwerem")
        return None
    
    soup = BeautifulSoup(page.content, 'html.parser')
    get_price = str(soup.find(class_="whole").get_text())

    return get_price

def pobierz_dane_Neonet(adres):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    page = requests.get(adres, headers=headers)

    if(page.status_code != 200):
        print("Błąd połączenia z serwerem")
        return None
    
    soup = BeautifulSoup(page.content, 'html.parser')
    get_price = str(soup.find(class_="uiPriceScss-integer-38D"))

    return get_price

def pobierz_dane_Media_Markt(adres):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    page = requests.get(adres, headers=headers)

    if(page.status_code != 200):
        print("Błąd połączenia z serwerem")
        return None
    
    soup = BeautifulSoup(page.content, 'html.parser')
    get_price = str(soup.find(class_=" ").get_text())
    
    return get_price

def pobierz_dane_Avans(adres):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    page = requests.get(adres, headers=headers)

    if(page.status_code != 200):
        print("Błąd połączenia z serwerem")
        return None
    
    soup = BeautifulSoup(page.content, 'html.parser')
    get_price = str(soup.find(class_="a-price_price").get_text())

    return get_price

def pobierz_dane_Allegro(adres):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    page = requests.get(adres, headers=headers)

    if(page.status_code != 200):
        print("Błąd połączenia z serwerem")
        return None
    
    soup = BeautifulSoup(page.content, 'html.parser')
    get_price = soup.find(class_="aria-hidden").get_text()   

    return get_price
'''