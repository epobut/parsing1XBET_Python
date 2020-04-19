from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://1x-bet-ua.com/ru/live/Football/"

driver = webdriver.Chrome()
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')

containers = soup.findAll("div", {"class": "c-events__item_col"})
for container in containers:
    teams = [x.get_text() for x in container.findAll(
        "span", {"class": "c-events__teams"}
    )]
    time = [x.get_text() for x in container.findAll(
        "div", {"class": "c-events__time"}
    )]
    odds = [x.attrs.get('data-coef') for x in container.findAll(
        "a", {"class": "c-bets__bet"}
    )]
    print(teams)
    print(time)
    print("     1 -    X -     2 -     1X -    12 -    2X -    Б -     Тотал -     М -     1 -     Фора -  2")
    print(odds)
    print()