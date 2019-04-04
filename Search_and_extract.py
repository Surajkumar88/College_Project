import pandas as pd
import requests as req
from bs4 import BeautifulSoup as bs

print("Enter the product: ")
search_pro = input()
#url = 'https://www.flipkart.com/search?q=nokia+6.1+plus&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
url = 'https://www.flipkart.com/search?q='+str(search_pro)+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
page = req.get(url)

soup = bs(page.text,'html.parser')

Name = []
pro_name = soup.find_all(class_ = '_3wU53n')
pro_name
for item in pro_name:
    Name.append(item.text)

i=1;
for item in Name:
    print(str(i)+":"+item)
    i = i+1

print("Enter an paste an option")
ch = input()
url1 = 'https://www.flipkart.com/search?q='+str(ch)+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
page1 = req.get(url1)

soup1 = bs(page1.text,'html.parser')

for div in soup1.find_all("div", {"class" :'_1UoZlX'}):
    for link in div.select("a._31qSD5"):
        print (link['href'])

print("Enter your choice")
ch1 = input()

url2 = 'https://www.flipkart.com'+str(ch1)
page2 = req.get(url2)

soup2 = bs(page2.text,'html.parser')

for div in soup2.find_all("div",{"class":"bhgxx2"}):
    for link in div.select("a"):
        print(link['href'])

print("Enter your choice")
ch2 = input()

url3 = 'https://www.flipkart.com'+str(ch2)

page3 = req.get(url3)

soup3 = bs(page3.text,'html.parser')

rev = soup3.find_all(class_ = 'qwjRop')
for item in rev:
    print(item)
