from bs4 import BeautifulSoup as bsoup
from selenium import webdriver

with open('output.csv','w') as output:
    browser = webdriver.Chrome()
    browser.get('https://www.reuters.com/markets/stocks')
    code = browser.page_source
    soup = bsoup(code,'lxml')
    match = soup.findAll('table')[0]


    # head = match.find('tr')
    # allhead = head.findAll('th')
    # for header in allhead:
    #     output.write(header.text + ";")

    body = match.find('tbody')
    rows= body.findAll('tr')
    for row in rows:
        cols = row.findAll('td')[0]
        name = cols.find('a')
        output.write(name.text + ";")
    output.write("\n")
    for row in rows:
        cols = row.findAll('td')[3]
        name = cols.find('span')
        output.write(name.text[1:5] + ";")
    output.write("\n")

    browser.close()
