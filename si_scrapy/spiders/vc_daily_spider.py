import scrapy
import utility.pref as pref
import logging
import si_scrapy.spiders.__init__ as init


class VcDailySpider(scrapy.Spider):
    name = 'vc_daily'
    dest_dir = pref.get_env_variable('SI_DATA_DIR')
    file_dir = dest_dir + '/vc_daily.dat'
    logger = logging.getLogger(__name__)

    def start_requests(self):
        url = 'http://www.vcnewsdaily.com/'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        try:
            f = open(self.file_dir, 'wb')
        except (OSError, IOError) as e:
            self.logger.error('Failed to open file:' + self.file_dir, e)
            exit(init.FILE_OPEN_ERROR)

        titles = response.xpath('//div[@id="headline"]/a/text()').extract()

        for title in titles:
            f.write(title + '\n')
        f.close()
