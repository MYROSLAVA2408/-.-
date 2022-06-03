import requests
from bs4 import BeautifulSoup
r = requests.get(url="https://mof.gov.ua/uk")
soup = BeautifulSoup(r.text, "lxml")
#print(soup.findAll("href")[0].getText)
print(soup.select('a')[0].get_text('href'))

