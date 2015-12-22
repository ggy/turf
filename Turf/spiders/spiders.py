from scrapy import Spider
from scrapy.selector import *

from scrapy import Request
from scrapy.http.headers import Headers

from Turf.items import *

import csv
import datetime
import locale
import json


RENDER_HTML_URL = "localhost:8050/render.html"

numdays = 365*5

class CoursesSpider(Spider):
    name = "aspiturf_courses"
    allowed_domains = ["aspiturf.com"]
    locale.setlocale(locale.LC_ALL, ("fr_FR", 'UTF-8'))
    base = datetime.date(2014, 12, 31)
    date_list = [base - datetime.timedelta(days=x) for x in range(0, numdays)]
    start_urls = ["http://aspiturf.com/index.php?datejour="\
        + str(i) + "#coursejour" for i in date_list]

    def parse(self, response):
        selector = Selector(response)
        questions = selector.xpath("//table[@id='datatables']/tbody/tr")

        for sel in questions:
            item = CourseItem()
            item['Date'] = sel.xpath("td[1]/text()").extract()
            item['Heure'] = sel.xpath("td[2]/text()").extract()
            item['Course'] = sel.xpath("td[3]/a/text()").extract()
            item['Reunion'] = sel.xpath("td[4]/text()").extract()
            item['Reun'] = sel.xpath("td[5]/text()").extract()
            item['Num'] = sel.xpath("td[6]/text()").extract()
            item['Type'] = sel.xpath("td[7]/text()").extract()
            item['Partant'] = sel.xpath("td[8]/text()").extract()
            item['Arrive'] = sel.xpath("td[9]/text()").extract()
            item['URL'] = sel.xpath("td[3]/a/@href").extract()
            item['Titre'] = sel.xpath("td[3]/a/@title").extract()

            yield item

class ReunionSpider(Spider):
    name = "aspiturf_reunions"
    allowed_domains = ["aspiturf.com"]

    cr = csv.reader(open("courses.csv","rb"))
    start_urls = ["http://aspiturf.com/" + str(i[0]) for i in cr]

    def start_requests(self):
            for url in self.start_urls:
                yield Request(url, self.parse, meta={
                    'splash': {
                        'endpoint': 'http://localhost:8050/render.html',
                        'args': {'wait': 1}
                    }
                })


    def parse(self, response):
        selector = Selector(response)
        question = selector.xpath("//table[@id='grdatatablesauto']/tbody/tr")

        self.logger.info("Extract %s", str(question.extract()))
        item = []
        for sel in question:
            item = ReunionItem()

            item['Cheval'] = sel.xpath("td[1]/a/text()").extract()
            item['Title_Cheval'] = sel.xpath("td[1]/a[1]/@title").extract()
            item['Jocket'] = sel.xpath("td[1]/a[2]/@compjoch").extract()
            item['Today'] = sel.xpath("td[1]/a[2]/@today").extract()
            item['Infojojo'] = sel.xpath("td[1]/a[2]/text()").extract()
            item['Title_Entraineur'] = sel.xpath("td[1]/a[2]/@title").extract()
            item['Entraineur'] = sel.xpath("td[1]/a[2]/b/text()").extract()

            item['Jvh'] = sel.xpath("td[2]/text()").extract()
            item['Jv'] = sel.xpath("td[3]/text()").extract()
            item['Jp'] = sel.xpath("td[4]/text()").extract()
            item['Evh'] = sel.xpath("td[5]/text()").extract()
            item['Ev'] = sel.xpath("td[6]/text()").extract()
            item['Ep'] = sel.xpath("td[7]/text()").extract()
            item['Oeil'] = sel.xpath("td[8]/b/text()").extract()
            item['rec'] = sel.xpath("td[9]/text()").extract()
            item['rapProb'] = sel.xpath("td[10]/text()").extract()
            item['rapDir'] = sel.xpath("td[11]/b/text()").extract()
            item['MusiquePT'] = sel.xpath("td[12]/text()").extract()
            item['MusiqueCal'] = sel.xpath("td[13]/a/@title").extract()
            item['MusiqueJoc'] = sel.xpath("td[14]/a/@title").extract()
            item['MusiqueEntr'] = sel.xpath("td[15]/a/@title").extract()

            item['Corde'] = sel.xpath("td[16]/text()").extract()
            item['Genre'] = sel.xpath("td[17]/text()").extract()
            item['Age'] = sel.xpath("td[18]/text()").extract()
            item['Handicap'] = sel.xpath("td[19]/text()").extract()
            item['NbCoursesCheval'] = sel.xpath("td[20]/text()").extract()
            item['NbVictoireCheval'] = sel.xpath("td[21]/text()").extract()
            item['Place'] = sel.xpath("td[22]/text()").extract()
            item['Victoire'] = sel.xpath("td[23]/text()").extract()
            item['PI'] = sel.xpath("td[24]/text()").extract()

            item['URL'] = response.meta

            yield item
