import scrapy
from scrapy.settings import Settings
from marketnews import settings as my_settings
from scrapy.crawler import CrawlerProcess
from marketnews.spiders.newsspider import NewsSpider
import datetime
from celery import Celery
from celery import group
from threading import Thread



app = Celery('tasks', broker='amqp://guest@localhost//')

@app.task
def spider():
        crawler_settings = Settings()
        crawler_settings.setmodule(my_settings)
        process = CrawlerProcess(settings=crawler_settings)
        process.crawl(NewsSpider)
        Thread(target=process.start).start()



app.conf.update(
        CELERYD_CONCURRENCY = 10,
        CELERYBEAT_SCHEDULE={
            'multiply-each-6-hours':{
            'task': 'tasks.spider',
            'schedule': datetime.timedelta(seconds=40),
            },
        },
)
