import scrapy

import requests

class AdiletzanSpider(scrapy.Spider):
    name = "AdiletZan"
    # allowed_domains = [""]
    start_urls = ["https://kodeksy-kz.com/ka/ugolovnyj_kodeks/1.htm"]

    def parse(self, response):
        # for link in response.css('h3.bloko-header-section-3 a::attr(href)'):
        #     yield response.follow(
        #         f'{link.get()}',
        #         callback=self.parse_article
        #     )

        for page in range(1, 468):
            url = f'https://kodeksy-kz.com/ka/ugolovnyj_kodeks/{page}.htm'
            response = requests.get(url)
            while response.status_code != 200:
                response = requests.get(url)

            yield response.follow(
                f'https://kodeksy-kz.com/ka/ugolovnyj_kodeks/{page}.htm',
                callback=self.parse_article
            )

    def parse_article(self, response):
        text_content = response.xpath('//div[@id="statya"]//text()').getall()

        cleaned_text = ' '.join(text_content).strip()
        data = {
            'text':cleaned_text
        }
        # pass
        yield data