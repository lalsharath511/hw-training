# import trafilatura
# from trafilatura import sitemaps
import json

# links = sitemaps.sitemap_search('https://www.coldwellbanker.com/sitemap_brokers_index.xml')
# # print(links)



from parsel import Selector
import requests

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
        # a=selector.xpath("//div[@class='media__content']/h1/text()").extract_first().strip("\n").strip(" ")
        b=len(selector.xpath("//a[contains(@class,'agent-link')]/@href"))
        self.list1=self.list1+b
        print(self.list1)
    def sitemap(self,url):
        response = requests.get(url=url, headers=self.headers)
        if response.status_code != 200:
            raise Exception('Failed to load page')
        selector = Selector(text=response.text)
        sitemap_url=selector.xpath("//sitemap/loc/text()").extract()
        for url in sitemap_url:
            self.coldwellbanker(url)
            
            
          
    def coldwellbanker(self, url, ):
        response = requests.get(url=url, headers=self.headers)
        # print(response.text)
        if response.status_code != 200:
            raise Exception('Failed to load page')
        selector = Selector(text=response.text)
        office_url=selector.xpath("//url/loc/text()")[1].extract()
        self.crawl(office_url)
    
        # b=[l for l in a if'office' in l]
        # print(b)
        
        # print(response.text)
        # a=selector.xpath('//article[contains(@class,"rng-agent-roster-agent-card js-sort-item")]/a/@href')
        # print(a)
        # for link in selector.xpath('//article[contains(@class,"rng-agent-roster-agent-card js-sort-item")]/a/@href'):
        #     print(link.text)https://www.coldwellbanker.com/coldwell-banker-1st-choice-realty-1127c/sitemap.xml

# mylines = [] 
# new=[]
# with open ('a.txt', 'rt') as myfile: 
#     for myline in myfile:
#         myline=myline.split("loc>")
#         mylines.append(myline)
        
# for i in myline:
#     if 'https://www.coldwellbanker.com' in i:
#         i=i.strip("</").strip(" ")
#         new.append(i)
 
url= 'https://www.coldwellbanker.com/sitemap_brokers_index.xml'     
obj = ExprealtyScraper()
obj.sitemap(url)




            
            
        # add its contents to mylines.
# print(new)
