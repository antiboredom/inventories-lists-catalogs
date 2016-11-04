from bs4 import BeautifulSoup
import urllib

start_url = 'https://newyork.craigslist.org/search/bar'
html = urllib.urlopen(start_url).read()

soup = BeautifulSoup(html)

titles = soup.select('.hdrlnk')

for title in titles:
    print title.text
