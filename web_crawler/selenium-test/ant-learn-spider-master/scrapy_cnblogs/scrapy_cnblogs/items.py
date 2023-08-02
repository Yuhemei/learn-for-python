# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyCnblogsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    datetime = scrapy.Field()
    like_count = scrapy.Field()
    comment_count = scrapy.Field()
    view_count = scrapy.Field()
