import scrapy
import requests


class ToScrap(scrapy.Spider):
    name = "scrapyexample"
    def start_requests(self):
        url = "https://books.toscrape.com/"
        res = requests.get(url)
        res.Selector.xpath("//section//article[@class='product_pod']/h3/a/@href").extract()
        print(res)
    #     response.xpath("//div//li[@class='next']/a/@href").extract()
    # crawler("https://books.toscrape.com/")
    
ToScrap()