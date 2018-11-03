from bs4 import BeautifulSoup
from requests import get
from urllib.request import urlopen, Request

req = Request('https://www.eia.gov/dnav/pet/PET_PRI_GND_DCUS_NUS_W.htm', headers={'User-Agent': 'Mozilla/5.0'})
response = urlopen(req).read()
response = response.decode('utf-8')
soup = BeautifulSoup(response, 'html.parser')
price = soup.find_all('td', attrs={'class':'Current2'})
print (float(price[0].text))