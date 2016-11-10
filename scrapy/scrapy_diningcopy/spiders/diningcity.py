# -*- coding: utf-8 -*-
import scrapy
import re
import datetime
from scrapy_diningcopy.items import DealInfoItem


_GLB_SPIDER_NAME     = "diningcopy"
_GLB_ALLOWED_DOMAIN  = ["diningcity.cn"]
_GLB_START_POINT_URL = "http://www.diningcity.cn/en/shanghai/events/"
_GLB_SEARCH_KEYWORDS = ["88/deals", "89/deals"]
_GLB_START_URL_LIST  = [_GLB_START_POINT_URL + _keyword for _keyword in _GLB_SEARCH_KEYWORDS]


class NeituiSpider(scrapy.Spider):

    name = _GLB_SPIDER_NAME
    allowed_domains = _GLB_ALLOWED_DOMAIN

    # start_urls = ["http://www.diningcity.cn/en/shanghai/events/89/deals"] # _GLB_START_URL_LIST
    start_urls = _GLB_START_URL_LIST

    # todayflag  = datetime.datetime.now().strftime('%m-%d')

    def parse(self, response):
        """
        Function:   This function is to parse the search result list

        IN:         response - crawl response
        Out:        NA

        Special:
        """

        # iterate each search result to see if there is any new for today
        # if yes, try to get the link and invoke parse_result_detail for details
        for result in response.xpath('//div[@class="en-shanghai-deals"]/div[@class="cent"]/div[@class="body"]/div[@class="main"]/ul[@class="dlist"]/li'):
            item = DealInfoItem()

            deal_name  = result.xpath('div[@class="info"]/a[@class="deal-name"]/text()').extract()[0]
            rest_name  = result.xpath('div[@class="info"]/a[@class="r-name"]/text()').extract()[0]
            disc_info  = result.xpath('div[@class="cover"]/div[@class="discount"]/span/text()').extract()
            list_price = result.xpath('div[@class="actions"]/div[@class="drape"]/div[@class="top"]/strong/text()').extract()[1]
            pic_link   = result.xpath('div[@class="cover"]/a[@class="pframe"]/img').extract()[0]
            pic_url    = pic_link[pic_link.find(u'src="')+5:pic_link.find(u'width="')-2]

            item['deal_name']  = deal_name.encode('utf-8')
            item['rest_name']  = rest_name.encode('utf-8')
            item['list_price'] = list_price.encode('utf-8')
            item['pic_url']    = pic_url.encode('utf-8')

            if len(disc_info) > 0:
                item['disc_info']  = disc_info[0].encode('utf-8')
            else:
                item['disc_info']  = "".encode('utf-8')

            yield item
