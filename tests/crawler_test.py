from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from si_scrapy.spiders import vc_daily_spider


process = CrawlerProcess(get_project_settings())
process.crawl(vc_daily_spider.VcDailySpider)
process.start()



