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

class ReunionItem(Item):
    Cheval = Field()
    Jocket = Field()
    Entraineur = Field()
    Title_Cheval = Field()
    Title_Entraineur = Field()
    Today = Field()
    Infojojo = Field()
    Entraineur = Field()

    Jvh = Field()
    Jv = Field()
    Jp = Field()
    Evh = Field()
    Ev = Field()
    Ep = Field()
    Oeil = Field()
    rec = Field()
    rapProb = Field()
    rapDir = Field()
    MusiquePT = Field()
    MusiqueCal = Field()
    MusiqueJoc = Field()
    MusiqueEntr = Field()
    Corde = Field()
    Genre = Field()
    Age = Field()
    Handicap = Field()
    NbCoursesCheval = Field()
    NbVictoireCheval = Field()
    Place = Field()
    Victoire = Field()
    PI = Field()

    URL = Field()
