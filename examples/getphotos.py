import urllib
from bs4 import BeautifulSoup
import time

url = "http://www.istockphoto.com/search/2/image?phrase=happy+cops"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

images = soup.select('.search-result-asset-link img')

imagenumber = 1

for image in images:
  imagesource = image.get('src')
  description = image.get('alt')
  print description
  imagefilename = "images/cop" + str(imagenumber) + ".jpg"
  imagenumber = imagenumber + 1
  urllib.urlretrieve(imagesource, imagefilename)
  time.sleep(.1)