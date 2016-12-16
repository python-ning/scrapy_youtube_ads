# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyNewbornItem(scrapy.Item):
    # 应用的名字
    Name = scrapy.Field()
    # 应用所在链接
    URL = scrapy.Field()
    # 应用的价格
    Price = scrapy.Field()
    # 应用的类型
    Genre = scrapy.Field()
    # 应用的安装次数
    Downloads = scrapy.Field()
    # 应用的评分
    Rating = scrapy.Field()
    # 应用的好评度
    Review_number = scrapy.Field()
    # 应用的更新日期
    Updated = scrapy.Field()
    # 应用的作者
    Author = scrapy.Field()
    # 应用的当前版本
    Version = scrapy.Field()
    # 视频的链接
    Video_url = scrapy.Field()
    # App 的 id
    App_id = scrapy.Field()



