# -*- coding: utf-8 -*-

import scrapy
from marketnews.items import MarketnewsItem, MarketnewsDescription, MarketnewsImage
from home.models import NewsCompany, DescriptionCompany, Company, ImageCompany
from scrapy.http import Request


companies = Company.objects.values_list('symbol', flat=True)

class NewsSpider(scrapy.Spider):
    name = "spider"


    def start_requests(self):
        del2 = NewsCompany.objects.all().delete()
        del1 = DescriptionCompany.objects.all().delete()
        del3 = ImageCompany.objects.all().delete()
        for i in range (len(companies)):
            yield Request(url = 'http://quotes.wsj.com/%s' % (companies[i]), callback=self.parseA)
            yield Request(url = 'http://quotes.wsj.com/%s/company-people' % (companies[i]), callback=self.parseB)
            yield Request(url = 'http://www.nasdaq.com/symbol/%s' % (companies[i]), callback=self.parseC)

    def parseA(self, response):
        company = response.xpath("//div[@class='mod_headerBox']/h2/span[@class='hdr_tkr_name']/text()").extract_first().strip()
        for li in response.xpath("//div[@id='news_module']/ul[@id='newsSummary_c']/li")[:10]:
            title = li.xpath(".//span[@class='headline']/a/text()").extract_first().strip()
            link = li.xpath(".//span[@class='headline']/a/@href").extract_first().strip()
            date = li.xpath(".//ul[@class='cr_metaData']/li[@class='cr_dateStamp']/text()").extract_first().strip()
	    yield MarketnewsItem(title=title,link=link, date=date,company=company)

    def parseB(self, response):
        company = response.xpath("//div[@class='cr_quotesHeader']/h1/span[@class='tickerName']/text()").extract_first().strip()
        name = response.xpath("//div[@class='mod_headerBox']/h3/span/text()").extract_first().strip()
        description = response.xpath("//div[@class='cr_description_full cr_expand']/p/text()").extract_first().strip()
        website = response.xpath("//div[@class='cr_profile_contact']/ul[@class='company-web']/li/a[@target='_blank']/@href").extract_first().strip()
        sector = response.xpath("//li[@class='cr_data_row cr_data_row-first']/div[@class='cr_data_field']/span[@class='data_data']/text()").extract_first().strip()
        employees = response.xpath("//li[@class='cr_data_row cr_data_row-first']/div[@class='cr_data_field cr_data_field-first']/span[@class='data_data']/text()").extract_first().strip()
        sales = response.xpath("//li[@class='cr_data_row']/div[@class='cr_data_field cr_data_field-first']/span[@class='data_data']/text()").extract_first().strip()
        industry = response.xpath("//ul[@class='cr_data_collection']/li[@class='cr_data_row']/div[@class='cr_data_field']/span[@class='data_data']/text()").extract_first().strip()
        yield MarketnewsDescription(company=company,name=name,description=description, sector=sector,employees=employees,
            sales=sales, industry=industry, website=website )

    def parseC(self, response):
        company = response.xpath("//div[@class='qbreadcrumb']/span[@class='qbreadcrumb']/b/text()").extract_first()
        image = response.xpath("//div[@class='floatL']/img[@class='quote-symbol-icon']/@src").extract_first()
        yield MarketnewsImage(image=image, company = company)
