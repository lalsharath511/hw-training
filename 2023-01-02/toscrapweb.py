import scrapy


class ToScrap(scrapy.Spider):
    name = "scrapyexample"
    def crawler(self,response):
        res=response.xpath("//section//article[@class='product_pod']/h3/a/@href").extract()
        print(res)
        response.xpath("//div//li[@class='next']/a/@href").extract()
    crawler("https://books.toscrape.com/")
    
ToScrap()