from scrapy import Spider
from scrapy.selector import *
from Turf.items import CourseItem
import datetime
import locale
numdays = 365
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor


class StackSpider(Spider):
    name = "aspiturf"
    allowed_domains = ["aspiturf.com"]
    locale.setlocale(locale.LC_ALL, ("fr_FR", 'UTF-8'))
    base = datetime.date(2009, 1, 1)
    date_list = [base + datetime.timedelta(days=x) for x in range(0, numdays)]
    start_urls = ["http://aspiturf.com/index.php?datejour="\
        + str(i) + "#coursejour" for i in date_list]



    def parse(self, response):
        selector = Selector(response)
        questions = selector.xpath("//table[@id='datatables']/tbody/tr")
        items = []
        for sel in questions:
            item = CourseItem()
            item['Date'] = sel.xpath("td[1]/text()").extract()
            item['Heure'] = sel.xpath("td[2]/text()").extract()
            item['Course'] = sel.xpath("td[3]/text()").extract()
            item['Reunion'] = sel.xpath("td[4]/text()").extract()
	    item['Reun'] = sel.xpath("td[5]/text()").extract()
            item['Num'] = sel.xpath("td[6]/text()").extract()
            item['Type'] = sel.xpath("td76]/text()").extract()
            item['Partant'] = sel.xpath("td[8]/").extract()
            item['Arrive'] = sel.xpath("td[9]").extract()
            item['URL'] = sel.xpath("td[3]/a/@href").extract()
            item['Titre'] = sel.xpath("td[3]/a/@title").extract()

            items.append(item)
            return items
