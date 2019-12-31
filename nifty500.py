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
    r1 = rows[0].findAll('th')[0:6]
    for col in r1:
      # data =col.findAll('a')
      output.write(col.text + ";")
    output.write("\n")

    for row in rows[1:]:
        cols =row.findAll('td')[0:6]
        for col in cols:
          # data =col.findAll('a')
          output.write(col.text + ";")
        output.write("\n")
        # print("")




    browser.close()
    output.close()
