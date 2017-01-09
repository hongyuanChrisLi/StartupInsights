from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from si_scrapy.si_scrapy.spiders import vc_daily_spider

#logging.config.fileConfig('logging.ini')
spider = vc_daily_spider
process = CrawlerProcess(get_project_settings())
process.crawl(spider)
process.start()
