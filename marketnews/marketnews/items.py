# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


#HERE IT IS NEEDED TO USE DJANGOITEM

import scrapy
from scrapy_djangoitem import DjangoItem
from home.models import NewsCompany, DescriptionCompany, ImageCompany

class MarketnewsItem(DjangoItem):
    django_model = NewsCompany

class MarketnewsDescription(DjangoItem):
    django_model = DescriptionCompany

class MarketnewsImage(DjangoItem):
    django_model = ImageCompany
