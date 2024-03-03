import scrapy
import json
import requests
import logging

class KodeksykzSpider(scrapy.Spider):
    name = "kodeksykz"
    start_urls = ["https://kodeksy-kz.com/ka/zakony.htm"]
    res = []
    title = ""
    def parse(self, response):
        logging.info("Parsing main page")
        zakons = response.xpath('//a[@class="nava"]/@href').getall()
        for zakon in range(2, 6):
            self.res = []
            yield response.follow(
                f'https://kodeksy-kz.com/{zakons[zakon]}',
                callback=self.parse_zakon,
                meta={'cookiejar': zakon}
            )
    def parse_zakon(self, response):
        self.title = response.css('h1::text').get()
        print(self.title, 'AAAAAAAAAA')
        logging.info("Parsing zakon page")
        law_status = response.xpath('//div[@id="law_status"]/div[@id="law_valid"]/text()').get()
        # self.title = response.xpath('//div[@id="')
        if law_status:  # действующий, иначе утратил силу
            pages = response.css('ul.no_dsk li b::text').getall()[-1]
            s = ""
            for i in pages:
                if i >= '0' and i <= '9':
                    s += i
            pages = int(s)
            for page in range(1, pages + 1):
                url = response.url[:-4] + '/' + str(page) + '.htm'
                resp = requests.get(url)
                if resp.status_code == 200:
                    yield response.follow(
                        f'{url}',
                        callback=self.parse_article,
                        meta=response.meta
                    )

    def parse_article(self, response):
        logging.info("Parsing article page")
        text_content = response.xpath('//div[@id="statya"]//*[not(self::h1)]/text()').getall()
        if not text_content:
            text_content = response.xpath('//div[@id="statya"]/text()').getall()
        statya = response.css('div#statya h1::text').getall()
        cleaned_text = ' '.join(text_content).strip()
        data = {
            statya[1]: cleaned_text
        }
        self.res.append(data)
        logging.info("Data appended to res list")
        # yield data

    def closed(self, reason):
        logging.info("Spider closed. Printing self.res...")
        # filename = self.get_filename(f'https://kodeksy-kz.com/{zakons[zakon]}')
        with open(self.title+'.json', 'w', encoding='utf-8') as f:
            json.dump(self.res, f,ensure_ascii=False,indent=4)
        print(self.res)
