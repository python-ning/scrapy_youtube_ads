#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import scrapy
import requests
import time
import subprocess
from scrapy.linkextractors import LinkExtractor
from scrapy_newborn.items import ScrapyNewbornItem
from scrapy.spiders import Rule, CrawlSpider
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class GooglePlayAdsSpider(CrawlSpider):
    name = "google_play_ads"
    allowed_domains = ["play.google.com"]
    start_urls = [
        'http://play.google.com/',
        'https://play.google.com/store/apps/details?id=air.net.machinarium.Machinarium.GP'
    ]

    rules = (
        Rule(LinkExtractor(allow=("https://play\.google\.com/store/apps/details",)), callback='parse_item',
             follow=True),
    )

    def parse_item(self, response):
        video_url = response.xpath('//span[@class="play-action-container"]/@data-video-url').extract_first()
        app_id = str(response.xpath('//div[@class="details-wrapper apps square-cover id-track-partial-impression id-deep-link-item"]/@data-docid').extract_first()).strip()+'.mp4'
        if response.url.find('reviewId') != -1: return;
        if video_url is None:
            return

        # 存视频相关代码
        os.chdir('/Users/ning.chen/Desktop/videos/')
        child = subprocess.Popen(['youtube-dl','--proxy','localhost:62911',str(video_url)])
        time.sleep(15)
        # else:
        #     with open('/Users/ning.chen/Desktop/videos/%s'%app_id,'wt') as f:
        #         response = requests.get(video_url)
        #         f.write(response.content)


        # print '1' * 100
        # print response.xpath('//div[@class="details-wrapper apps square-cover id-track-partial-impression id-deep-link-item"]/@data-docid').extract_first()
        # print response.xpath('//span[@class="play-action-container"]/@data-video-url').extract_first()
        # print response.xpath('//div[@class="id-app-title"]/text()').extract_first()
        # print response.url
        # print response.xpath("//div[@itemprop='numDownloads']/text()").extract_first()
        # print response.xpath("//div[@itemprop='datePublished']/text()").extract_first()
        # print response.xpath('//div[@itemprop="softwareVersion"]/text()').extract_first()
        # print response.xpath("//span[@class='reviews-num']/text()").extract_first()
        # print response.xpath("//div[@class='score']/text()").extract_first()
        # print response.xpath('//div[@itemprop="author"]/a/span/text()').extract_first()
        # print response.xpath('//span[@itemprop="genre"]/text()').extract_first()
        # prices = response.xpath('//button[@class="price buy id-track-click id-track-impression"]/span[2]/text()').re('\d+\.\d+')
        # print float(prices[0]) if prices!=[] else 0
        # print '1' * 100
        item = ScrapyNewbornItem()
        # 视频的链接
        item["Video_url"] = response.xpath('//span[@class="play-action-container"]/@data-video-url').extract_first()
        # App 的 id
        item["App_id"] = response.xpath('//div[@class="details-wrapper apps square-cover id-track-partial-impression id-deep-link-item"]/@data-docid').extract_first()
        # APP 的名字
        item["Name"] = response.xpath('//div[@class="id-app-title"]/text()').extract_first()
        # App 的详情连接
        item["URL"] = response.url
        # 安装次数
        item["Downloads"] = response.xpath("//div[@itemprop='numDownloads']/text()").extract_first()
        # 更新日期
        item["Updated"] = response.xpath("//div[@itemprop='datePublished']/text()").extract_first()
        # 当前版本
        version = response.xpath('//div[@itemprop="softwareVersion"]/text()').extract_first()
        item["Version"] = version if version else ''
        # 好评度
        review_number = response.xpath("//span[@class='reviews-num']/text()").extract_first()
        item["Review_number"] = review_number if review_number else ''
        # 评分
        rating = response.xpath("//div[@class='score']/text()").extract_first()
        item["Rating"] = rating if rating else ''
        # 作者
        item["Author"] = response.xpath('//div[@itemprop="author"]/a/span/text()').extract_first()
        # 应用类型
        item["Genre"] = response.xpath('//span[@itemprop="genre"]/text()').extract_first()
        price = response.xpath('//button[@class="price buy id-track-click id-track-impression"]/span[2]/text()').re('\d+\.\d+')
        # print prices if prices != [] else 0
        # price = response.xpath('//button[@class="price buy id-track-click id-track-impression"]/span[2]/text()').re('\d+\.\d+')
        item['Price'] = float(price[0]) if price != [] else 0
        yield item

