import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
#import xlsxwriter
Name = []
Price = []
Rating = []
i=1
while i<10:

    url = 'https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.serviceability%5B%5D%3Dfalse&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D30000&page='+str(i)
    page = requests.get(url)

    soup = bs(page.text,'html.parser')


    mob_name = soup.find_all(class_ = '_3wU53n')
    for item in mob_name:
        Name.append(item.text)


    mob_price = soup.find_all(class_ = '_1vC4OE _2rQ-NK')
    for item in mob_price:
        Price.append(item.text)


    mob_rating = soup.find_all(class_ = 'hGSR34')
    for item in mob_rating:
        Rating.append(item.text)
    i = i+1

Mobile_Info = []
for name, price, rating in zip(Name, Price, Rating):
    Mobile_Info.append({'Name':name, 'Price':price, 'Rating':rating})
    df = pd.DataFrame(Mobile_Info)


Mobile_csv =df.to_csv (r'Web-Scrapping\Mobile.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path
