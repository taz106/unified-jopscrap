import scrapy
# from jobScrapper.items import QuoteItem 


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            # yield {
            #     'text': quote.css('span.text::text').get(),
            #     'author': quote.css('small.author::text').get(),
            #     'tags': quote.css('div.tags a.tag::text').getall(),
            # }
            item_content = quote.css('span.text::text').extract_first()
            item_author = quote.css('small.author::text').extract_first()
            # quoteItem = QuoteItem(content= item_content,author=item_author)
            pass
            