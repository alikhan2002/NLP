import scrapy

import requests

class AdiletzanSpider(scrapy.Spider):
    name = "AdiletZan"
    # allowed_domains = [""]
    # start_urls = ["https://kodeksy-kz.com/ka/ugolovnyj_kodeks/1.htm"]
    start_urls = ["https://adilet.zan.kz/rus/docs/K1400000226"]

    def parse(self, response):
        heading = response.xpath('//h3/text()').getall()
        text_content = response.xpath('//div[@class="gs_12"]//text()').getall()
        cleaned_text = ' '.join(text_content).strip()
        data = {
            'heading':heading,
            'text': cleaned_text
        }
        yield data
        # for page in range(1, 468):
        #     # print(page)
        #     yield response.follow(
        #         f'https://kodeksy-kz.com/ka/ugolovnyj_kodeks/{page}.htm',
        #         callback=self.parse_article,
        #         # priority=page
        #     )
        # yield data

    def parse_article(self, response):
        text_content = response.xpath('//div[@id="statya"]//text()').getall()
        cleaned_text = ' '.join(text_content).strip()
        data = {
            'text':cleaned_text
        }
        # pass
        yield data



# import requests
# from bs4 import BeautifulSoup
#
#
# url = 'https://adilet.zan.kz/rus/docs/K1400000226'
# soup = BeautifulSoup(requests.get(url).content, 'html.parser')
#
#
# out = {}
# tag = soup.select_one('h3')
# current_header = tag.text
# while True:
#     tag = tag.find_next_sibling()
#     if not tag:
#         break
#     if tag.name == 'h3':
#         current_header = tag.text
#     else:
#         out.setdefault(current_header, '')
#         out[current_header] += tag.get_text(strip=True)
# print(out)





{
    "ОБЩАЯ ЧАСТЬ": [
       "РАЗДЕЛ 1. УГОЛОВНЫЙ ЗАКОН": [
                   " Статья 1. Уголовное законодательство Республики Казахстан": [
                        "1. Уголовное законодательство Республики Казахстан состоит из настоящего Уголовного кодекса Республики Казахстан. Иные законы, предусматривающие уголовную ответственность, подлежат применению только после их включения в настоящий Кодекс. 2. Настоящий Кодекс основывается на  Конституции  Республики Казахстан и общепризнанных принципах и нормах международного права.  Конституция  Республики Казахстан имеет высшую юридическую силу и прямое действие на всей территории Республики. В случае противоречий между нормами настоящего Кодекса и Конституции Республики Казахстан действуют положения  Конституции . Нормы настоящего Кодекса, признанные неконституционными, в том числе ущемляющими закрепленные Конституцией Республики Казахстан права и свободы человека и гражданина, утрачивают юридическую силу и не подлежат применению. Нормативные постановления Конституционного Суда и Верховного Суда Республики Казахстан являются составной частью уголовного законодательства Республики Казахстан. 3. Международные договоры, ратифицированные Республикой Казахстан, имеют приоритет перед настоящим Кодексом. Порядок и условия действия на территории Республики Казахстан международных договоров, участником которых является Республика Казахстан, определяются законодательством Республики Казахстан. Сноска. Статья 1 с изменением, внесенным Законом РК от 27.12.2018  № 205-VI  (вводится в действие по истечении десяти календарных дней после дня его первого официального опубликования); от 05.11.2022  № 157-VII  (вводится в действие с 01.01.2023)."
                    ]
        ]
    ]
}