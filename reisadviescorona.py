from colorama import Fore, Back, Style
import requests
from bs4 import BeautifulSoup
import time


def grab_site(land):
    url = f"https://www.nederlandwereldwijd.nl/landen/{land.lower()}/reizen/reisadvies"
    req = requests.get(url)
    if req.status_code == 404:
        print("Dit land komt niet voor in de lijst van nederlandwereldwijd.nl")
        exit()
    else:
        soup = BeautifulSoup(req.content, 'html.parser')
        anker = soup.find(id="anker-veiligheidsrisico’s")
        string = str(anker.find_next('h3'))
        split_string = string.split(">", 1)
        sub_string = split_string[1]
        split_string = sub_string.split("<", 1)
        sub_string = split_string[0]
        return sub_string


def main():
    land = input("Geef de naam van een land: ")
    inputloop = input("Wil je dit loopen? 0 voor nee, 1 voor ja: ")
    if inputloop == '0':
        safety_code(land)
    elif inputloop == '1':
        looptime = input("Hoe vaak wil je checken (in seconden): ")
        while inputloop == '1':
            print(Fore.WHITE, time.ctime())
            try:
                safety_code(land)
                if inputloop == '1':
                    time.sleep(int(looptime))
            except KeyboardInterrupt:
                print(Fore.WHITE, "Keyboard interrupt exception caught")
                exit()
    else:
        print("Dat is geen juiste optie")
        exit()


def safety_code(land):
    safetycode = grab_site(land)
    color = (safetycode.split(":", 1))[0]
    if color == 'Oranje' or color == 'Rood':
        print(Fore.RED, safetycode)
    elif color == 'Geel':
        print(Fore.YELLOW, safetycode)
    elif color == 'Groen':
        print(Fore.GREEN, safetycode)

main()





