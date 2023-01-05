import requests
from parsel import Selector
import json

class Mytheresa:
    def __init__(self):
        self.url = 'https://www.mytheresa.com/int_en/men/shoes.html'
        self.headers={
        'user-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }
    
    def parse(self):
        response= requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            text = response.text
            selector = Selector(text=text)
            url_list=selector.xpath('//a[contains(@class,"product-image")]/@href').extract()
            for link in url_list:
                 crawl(link,self.headers)

            # next_page=selector.xpath('//li[contains(@class,"next")]/a/@href').get()
            # if next_page is not None:
            #     parse(next_page, self.headers)
    def crawl(self)