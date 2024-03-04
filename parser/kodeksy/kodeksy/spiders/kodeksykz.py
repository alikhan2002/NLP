import scrapy
import json
import requests
import logging
from bs4 import BeautifulSoup

class KodeksykzSpider(scrapy.Spider):
    name = "kodeksykz"
    start_urls = ["https://kodeksy-kz.com/ka/zakony.htm"]
    res = []
    title = ""
    all_zakons = []
    def yield_zakon(self):
        if self.all_zakons:
            # print(self.all_zakons, 'JKANKJAYF(*HUIOUHFOIAF)A*HF')
            url = self.all_zakons.pop(0)

            # print("Scraping category--------------AAAAAAAAAAAAAAAA %s " % (url))
            return scrapy.Request(url, self.parse_zakon)
        else:
            print("all done")
    def parse(self, response):
        logging.info("Parsing main page")
        zakons = response.xpath('//a[@class="nava"]/@href')
        self.all_zakons = list(response.urljoin(zakon.extract()) for zakon in zakons)
        self.all_zakons = self.all_zakons[2:]
        # print(self.all_zakons, 'AAAAAAABBBBBBBBBBBBCCCCCCCC')
        yield self.yield_zakon()


        # for zakon in range(2, 4):
        #     self.res = []
        #     yield response.follow(
        #         f'https://kodeksy-kz.com/{zakons[zakon]}',
        #         callback=self.parse_zakon,
        #     )
    def parse_zakon(self, response):
        self.title = response.css('h1::text').get()
        # print(self.title, '-------------AAAAAAAAAA')
        logging.info("Parsing zakon page")
        law_status = response.xpath('//div[@id="law_status"]/div[@id="law_valid"]/text()').get()
        if law_status:  # действующий, иначе утратил силу
            pages = response.css('ul.no_dsk li b::text').getall()[-1]
            s = ""
            for i in pages:
                if i >= '0' and i <= '9':
                    s += i
            pages = int(s)
            # print(pages,'adadadadad-adad-a-da-d-a--da-')
            for page in range(1, pages + 1):
                # print(page, 'AKKLAJLKAJLKJHAHKLSKHAKSHKJ')
                url = response.url[:-4] + '/' + str(page) + '.htm'
                resp = requests.get(url)
                if resp.status_code == 200:
                    yield response.follow(
                        url,
                        callback = self.parse_article
                    )

            self.to_json()
        yield self.yield_zakon()

    def parse_article(self, response):
        logging.info("Parsing article page")
        text_content = response.xpath('//div[@id="statya"]').get()
        tags = ['h1', 'h3']
        soup = BeautifulSoup(text_content, 'html.parser')

        for t in tags:
            [s.extract() for s in soup(t)]

        text = ''.join([el.text for el in soup.find_all()])
        # print(text)
        # if not te xt_content:
        #     text_content = response.xpath('//div[@id="statya"]/text()').getall()
        statya = response.css('div#statya h1::text').getall()
        cleaned_text = ''.join(text).strip()
        # print(cleaned_text)
        data = {
            statya[1]: cleaned_text
        }
        self.res.append(data)
        logging.info("Data appended to res list")
        # yield data

    def to_json(self):
        logging.info('saving to json')
        with open(self.title+'.json', 'w', encoding='utf-8') as f:
            json.dump(self.res, f,ensure_ascii=False,indent=4)
        self.res = []
        # print(self.res)