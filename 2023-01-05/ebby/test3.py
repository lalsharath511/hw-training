from parsel import Selector
import requests

import xml.etree.ElementTree as ET

class ExprealtyScraper:

    def __init__(self):
        self.list1=0
        
        self.headers = {
        "user-agent": "Mozilla / 5.0 (X11; Linux x86_64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    def crawl(self, url, ):
        response = requests.get(url=url, headers=self.headers)
        if response.status_code != 200:
            raise Exception('Failed to load page')
        selector = Selector(text=response.text)
        print("hi")
        # a=selector.xpath("//div[@class='media__content']/h1/text()").extract_first().strip("\n").strip(" ")
        b=selector.xpath("//section[contains(@class,'rng-bio-account-content-office')]/h1/text()").extract()
        # self.list1=self.list1+b
        print(b)

            
          
    def coldwellbanker(self, url, ):
        a=url
        tree = ET.parse('data.xml')
        root = tree.getroot()
        print(root.url)
        
        response = requests.get(url=url, headers=self.headers)
        # print(response.text)
        if response.status_code != 200:
            raise Exception('Failed to load page')
        selector = Selector(text=response.text)
        agent_url=selector.xpath('//a[@class="button hollow"]/@href').extract()
        print(agent_url)
        for link in agent_url:
            print(link)
            bio_url=f'https://www.ebby.com/{link}'
            self.crawl(bio_url)
            
        
        
url='file:///home/czone/.cache/.fr-qFx8cC/sitemapbio%20(3).xml'
obj = ExprealtyScraper()
obj.coldwellbanker(url)
