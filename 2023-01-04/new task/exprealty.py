from parsel import Selector
import requests

class ExprealtyScraper:

    def __init__(self):
        self.headers = {
            "sec-ch-ua-platform": "Linux",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
        
    def exprealty(self, url, ):
        response = requests.get(url=url, headers=self.headers)
        if response.status_code != 200:
            raise Exception('Failed to load page')
        selector = Selector(text=response.text)
        # print(response.text)
        # print(selector.extract())
        
        print(selector.xpath('//div[@class= "sidx-search-result-grid-item sidx-with-overlay"]/a/text()').extract())
        for link in selector.xpath('//div[contains(@class,"sidx-search-result-grid-item sidx-with-overlay")]/a/@href'):
            print(link.text)
        
url = 'https://exprealty.com/properties/?page=1'
obj = ExprealtyScraper()
obj.exprealty(url)