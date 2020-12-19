# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class PonyItem(scrapy.Item):
#    # define the fields for your item here like:
#    # name = scrapy.Field()
#    pass


class TiantangItem(scrapy.Item):
    # define the fields for your item here like:
    name = 'tiantang'


class MzituLoopItem(scrapy.Item):

    name = 'mzitu_loop'
    cover_fig_url = scrapy.Field()
    jump_url = scrapy.Field()
    title = scrapy.Field()
    day = scrapy.Field()


class MzituItem(scrapy.Item):

    name = 'mzitu'

    url = scrapy.Field()
    large_pics = scrapy.Field()
    category = scrapy.Field()
    category_link = scrapy.Field()
    title = scrapy.Field()
    publish_time = scrapy.Field()
    tags = scrapy.Field()
    tags_link = scrapy.Field()


class MzituFigureItem(scrapy.Item):

    name = 'mzitu_figure'
    noid = scrapy.Field()
    large_pic = scrapy.Field()
