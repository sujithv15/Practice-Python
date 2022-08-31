from bs4 import BeautifulSoup
import requests

url = 'http://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html)
for string in soup.body():
    print(string)
