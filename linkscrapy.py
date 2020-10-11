import scrapy

class LinkscrapySpider(scrapy.Spider):
    name = 'linkscrapy'
    page_number = 2
    allowed_domains = ['amazon.com.br']
    start_urls = ['https://www.amazon.com.br/s?k=machine+learning&i=stripbooks&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss']

    def parse(self, response):

        links = response.css("h2 > a::attr(href)").extract()

        for link in links:

            yield {"link":'https://www.amazon.com.br' + link}

        next_page = 'https://www.amazon.com.br/s?k=machine+learning&i=stripbooks&page=' + str(LinkscrapySpider.page_number) + '&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1602031469&ref=sr_pg_' + str(LinkscrapySpider.page_number)

        if LinkscrapySpider.page_number <= 100:
            LinkscrapySpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
