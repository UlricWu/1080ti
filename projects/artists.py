import requests
from bs4 import BeautifulSoup
import csv

def getlinks(links):
    req = requests.get(links)
    return BeautifulSoup(req.text, 'lxml')

def getName(links):
    soup = getlinks(links)
    web = []
    temp = []
    url = 'https://www.straussart.co.za/artists/view/'

    for link in soup.find_all('a'):
        if not link.get('href'): continue

        if link.get('href')[:4] == 'http':
            temp = link.get('href')
        else:
            temp = links + link.get('href')
        ## filter anything that are not the artist's names
        if url in temp:
            web.append(temp)
        ## return unique artist's names
    return list(set(web))

def getDate(links):
    soup = getlinks(links)

    ## title2 of website is the name of an artist
    name = (soup.h2.contents[0])
    try:
        date = soup.p.contents[0]
    except:
        date = 'Na'

    return [name, date]

def getArtists():
    alphas = ['a-b', 'c-f', 'g-k', 'l-m', 'n-r', 's-t', 'u-z']
    url = 'https://www.straussart.co.za/artists/live/'
    artists = []
    names = []
    for alpha in alphas:
        names.append(getName(url + alpha))
    names = [x for y in names for x in y]
    for name in names:
        artists.append(getDate(name))
    return artists

def getAfrica(artists):
    results = []
    for artist in artists:
        if 'South African' not in artist[1]:
            continue
        ##All I need is the artists from South African, so I just filter it.
        ## the numbers of total artists are 650 from SA.
        results.append([artist[0], artist[1].replace('South African', '')])
    return results

def getData(results):
    with open("out.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(results)

if __name__ == '__main__':
    artists = getArtists()
    artists_south_africa =getAfrica(artists)
    getData(artists_south_africa )