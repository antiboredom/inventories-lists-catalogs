from bs4 import BeautifulSoup
import urllib

base_url = 'https://newyork.craigslist.org'
start_url = base_url + '/search/bar'
html = urllib.urlopen(start_url).read()

soup = BeautifulSoup(html)

links = soup.select('.hdrlnk')

for link in links:
    url = base_url + link.get('href')
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    try:
        img = soup.select('.first.visible img')[0]
        print img.get('src')
    except:
        continue

