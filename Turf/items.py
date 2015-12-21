# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class CourseItem(Item):
    Date = Field()
    Heure = Field()
    Course = Field()
    Titre = Field()
    Reunion = Field()
    Reun = Field()
    Num = Field()
    Type = Field()
    Partant = Field()
    Arrive = Field()
    URL = Field()
