import urllib
from bs4 import BeautifulSoup
import time

def get_items(url):
  html = urllib.urlopen(url).read()

  soup = BeautifulSoup(html)

  titles = soup.select('.hdrlnk')

  for title in titles:
    print title.text.encode('utf8')

base_url = "http://newyork.craigslist.org/search/sss?s="
currentpage = 0

while currentpage < 2500:
  url = base_url + str(currentpage)
  get_items(url)
  currentpage = currentpage + 100
  time.sleep(.1)

#get_items("http://newyork.craigslist.org/search/bar")
#get_items("http://newyork.craigslist.org/search/bar?s=100")
#get_items("http://newyork.craigslist.org/search/bar?s=200")

