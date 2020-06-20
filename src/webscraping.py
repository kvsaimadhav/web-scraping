from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/Users/madhav/PycharmProjects/web-scraping/src/chromedriver")  # give the location of chrome driver in your pc

products = []  # List to store name of the product
prices = []  # List to store price of the product
# ratings=[] #List to store rating of the product

url = "https://www.flipkart.com/search?q=Laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="
for i in range(1, 27):
    pageno = str(i)
    totalurl = url + pageno
    driver.implicitly_wait(10)
    driver.get(totalurl)

    content = driver.page_source
    features = "html.parser"
    soup = BeautifulSoup(content, features)
    for a in soup.findAll('a', href=True, attrs={'class': '_31qSD5'}):
        name = a.find('div', attrs={'class': '_3wU53n'})
        price = a.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})
        # rating=a.find('div',attrs={'class':'hGSR34'})
        products.append(name.text)
        prices.append(price.text)
    # ratings.append(rating.text)

df = pd.DataFrame({'Product Name': products, 'Price': prices})  # ,'Rating':ratings})
df.to_csv('../output/products.csv', index=False, encoding='utf-8')
