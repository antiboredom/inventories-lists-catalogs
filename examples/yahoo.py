import urllib
from bs4 import BeautifulSoup
import time
import csv

url = "https://answers.search.yahoo.com/search?p=lol&ei=UTF-8&nojs=1"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

items = soup.select('.AnswrsV2')

outfile = open('questions.csv', 'wb')
csvwriter = csv.writer(outfile)
csvwriter.writerow(['questions', 'answers'])

for item in items:
  question = item.select('h3')[0].text
  answer = item.select('.compText')[0].text

  csvwriter.writerow([question, answer])