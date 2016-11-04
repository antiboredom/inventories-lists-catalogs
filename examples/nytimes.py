from bs4 import BeautifulSoup
import urllib

start_url = 'http://www.foxnews.com/politics/2016/10/28/exclusive-comey-memo-to-fbi-staffers-says-election-timing-required-disclosure-renewed-probe.html'
html = urllib.urlopen(start_url).read()

soup = BeautifulSoup(html)
text = soup.select('.main')[0].text

words = text.split(' ')
words = sorted(words)

for word in words:
    word = word.strip()
    if word != '':
        print word
