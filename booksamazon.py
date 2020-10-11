import scrapy
import json
import time

lines = []
with open('/home/renan/Desktop/Portfolio/Curso Mário/scrapy_amazon/amazonscrapy/amazonscrapy/links.jl', 'r') as f:
    for line in f:
        lines.append(json.loads(line))
links = [l['link'] for l in lines]

class BooksamazonSpider(scrapy.Spider):
    name = 'booksamazon'
    cont = 1
    allowed_domains = ['amazon.com.br']
    start_urls = [links[0]]

    def parse(self, response):
        title = response.css("#productTitle::text").extract()
        #price = response.css(".price3P::text").extract() 
        #description = response.xpath("//*[@id='iframeContent']/p/text()[5]").extract() 
        #pages = response.css("#detailBullets_feature_div li:nth-child(1) .a-text-bold+ span::text").extract()
        #rating = response.css("div.a-fixed-left-grid-col.aok-align-center.a-col-right > div > span > span::text").extract()
        yield {"title":title}
        
        next_book = links[self.cont]
        #if BooksamazonSpider.cont < len(links):
        if self.cont < 10:
            self.cont += 1
            yield response.follow(next_book, callback=self.parse)
            
            