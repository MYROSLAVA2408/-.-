import requests
from bs4 import BeautifulSoup
r = requests.get(url="https://mof.gov.ua/uk")
soup = BeautifulSoup(r.text, "lxml")
print(soup.select('lt')[0].getText)
print(soup.select('p')[0].getText)
print(soup.select('gt')[0].getText)