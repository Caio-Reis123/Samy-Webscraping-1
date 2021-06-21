import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'QuotesSpider'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):

        all_quotes = response.xpath('//div[@class="quote"]')
        for quotes in all_quotes:
            quote = quotes.xpath('.//span[@class="text"]/text()').extract_first()
            author = quotes.xpath('.//small[@class="author"]/text()').extract_first()
            yield {
                'Quote': quote,
                'Author': author
            }

    