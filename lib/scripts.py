#Plik przechowujący funkcję sprawdzające link i tworzące pliki bazy danych

def sprawdz_sklep(adres):
    if(adres.find("rtveuroagd") != -1):
        return "RTV EURO AGD"
    elif(adres.find("komputronik") != -1):
        return "Komputronik"
    '''
    elif(adres.find("mediamarkt") != -1):
        return "Media Markt"
    elif(adres.find("neonet") != -1):
        return "Neonet"
    elif(adres.find("x-kom") != -1):
        return "X-Kom"
    '''
    else:
        return None