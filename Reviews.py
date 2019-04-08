import requests as req
from bs4 import BeautifulSoup as bs
import json
import math

# Get Total Pages
url = 'https://www.flipkart.com/nokia-6-1-plus-black-64-gb/product-reviews/itmf8r36g9gfpafg?pid=MOBF8FCFB9KWUTVQ'

page = req.get(url)
soup = bs(page.text, 'html.parser')


scripts = soup.find_all('script')
for script in scripts:
    if 'window.__INITIAL_STATE__ = ' in script.text:
        script_str = script.text
        jsonStr = script_str.split('window.__INITIAL_STATE__ = ')[1]
        jsonStr = jsonStr.rsplit(';',1)[0]

        jsonObj = json.loads(jsonStr)
        total_pages = math.ceil(jsonObj['ratingsAndReviews']['reviewsData']['totalCount'] / 10)





total_pages=5  # <------ remove this to get all pages, or set you page limit

for page in range(1,total_pages+1):
    page_url = url + '&page=%s' %page

    print ('Page %s' %page)
    page = req.get(page_url)
    soup = bs(page.text, 'html.parser')


    scripts = soup.find_all('script')
    for script in scripts:
        if 'window.__INITIAL_STATE__ = ' in script.text:
            script_str = script.text
            jsonStr = script_str.split('window.__INITIAL_STATE__ = ')[1]
            jsonStr = jsonStr.rsplit(';',1)[0]

            jsonObj = json.loads(jsonStr)


    for each in jsonObj['ratingsAndReviews']['reviewsData']['reviewsData']['nonAspectReview']:
        print (each['value']['text'],'\n')
