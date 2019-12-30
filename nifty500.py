from bs4 import BeautifulSoup as bsoup
from selenium import webdriver

with open('output.txt','w') as output:
    browser = webdriver.Chrome()
    browser.get('https://finance.yahoo.com/world-indices/')
    code = browser.page_source
    soup = bsoup(code,'lxml')
    match = soup.findAll('div',{"id":"render-target-default"})
    match = match[0].findAll('table')
    rows = match[0].findAll('tr')
    # match = match.findAll('div',{"class":"Ovx(a)"})
    # match = match.findAll('div',{"class":"Ovx(a)"})
    for row in rows[1:]:
        data =row.findAll('td')
        data =data[0].findAll('a')
        print(data[0].text)




    browser.close()
    output.close()
