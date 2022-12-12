import time
import requests
from bs4 import BeautifulSoup
import re

def headers():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    return headers

def getData(url):
    response = requests.get(url, headers=headers())
    time.sleep(3)
    return response

def soupData(response):
    soup = BeautifulSoup(response.text, 'lxml')
    return soup

def main(url):
    response = getData(url)

    soup = soupData(response)
    print(soup)
    return str(soup)

if __name__ == '__main__':
    url = 'https://www.bbc.co.uk/news/uk-62345010'
    l = re.findall(r'eq5iqo00">(.*?)</p>', main(url), re.S)
    main(url)
    for i in l:
        print(i)



