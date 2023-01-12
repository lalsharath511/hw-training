import gzip
import io
import requests
import re
from parsel import Selector
import json
class Bayut():
    def __init__(self):
        self.headers = {
		'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
		}
        self.count=0
    def parse(self, url, ):
        response = requests.get(url=url, headers=self.headers)
        selector = Selector(text=response.text)
        link=selector.xpath("//a[@aria-label='Listing link']/@href").extract()
        link=[*set(link)]
        for url in link:
            
            url=f'https://www.bayut.sa{url}'
            self.parse_property(url)
    def parse_property(self, url, ):
        response = requests.get(url=url, headers=self.headers)
        selector = Selector(text=response.text)
        url = re.findall("[0-9]", url)
        id="".join(url)
        


       
    def parse_link(self,path):
        response = requests.get(url=path, headers=self.headers)
        if response.status_code != 200:
            raise Exception("Error")
        selector = Selector(text=response.text)
        link=selector.xpath("//a[@title='Next']/@href").extract_first()
        print(link)
        url=f'https://www.bayut.sa{link}'
        print(url)
        self.count=self.count+1
        print(self.count)
        self.parse_link(url)
        
        
path = 'https://www.bayut.sa/en/ksa/properties-for-sale/'
ebby = Bayut()
ebby.parse_link(path)


# reference_number
# id
# url
# broker_display_name
# broker
# category
# category_url
# title
# description=selector.xpath("//div[@aria-label='Property description']//div[@dir='auto']/span/text()").extract()

# location
# price=selector.xpath("//span[@aria-label='Price']/text()").extract_first().replace(",","")
# currency=selector.xpath("//span[@aria-label='Currency']/text()").extract_first()
# price_per
# bedrooms=selector.xpath("//span[@aria-label='Beds']/span/text()").extract_first()
# bathrooms=selector.xpath("//span[@aria-label='Baths']/span/text()").extract_first()
# furnished
# rera_permit_number
# dtcm_licence
# scraped_ts
# amenities
# details
# agent_name
# number_of_photos
# user_id
# phone_number
# date
# iteration_number
# depth
# sub_category_1
# property_type
# sub_category_2
# published_at
# listing_availability

                