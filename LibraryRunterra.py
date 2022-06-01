import time
from urllib.request import urlopen
from bs4 import BeautifulSoup


def typePrint(text, delay=.05):
    for letter in text:
        print(letter, end='')
        time.sleep(delay)
    print("\n")


def main():
    typePrint("Hello! Welcome to the Runeterra virtual library experience!")
    while True:
        try:
            champ_select = input("Who's bio would you like to read? ").lower()
            page = urlopen(f'https://universe.leagueoflegends.com/en_US/story/champion/{champ_select}/')
            soup = BeautifulSoup(page, 'html.parser')
            desc = soup.find("meta", property="og:description")
            b = desc["content"].split(".")
            bio = [x for x in b]
            for x in bio:
                print(x)
        except:
            print("I'm sorry, that's not a valid input. Please try again.")
            continue
        else:
            break

    restart = input('Do you wish to read another bio?(y/n) ').lower()
    if restart == 'y':
        main()

    else:
        exit()


main()
