import urllib

url = 'https://newyork.craigslist.org/search/aap'
html = urllib.urlopen(url).read()

print html
