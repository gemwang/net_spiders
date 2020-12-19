# -*- coding: utf-8 -*-
import scrapy
import re
from pony.items import MzituLoopItem, MzituItem


class MzituSpider(scrapy.Spider):
    name = 'mzitu'
    allowed_domains = []
    home_url = 'https://www.mzitu.com/'
    start_urls = ['']

    def parse(self, response):
        post_block = response.xpath('//div[@class="postlist"]').xpath('ul/li')
        post_size = len(post_block)
        print('url: %s, size: %d' % (response.url, post_size))
        for idx in range(post_size):
            item_loop = MzituLoopItem()

            item_loop['cover_fig_url'] = post_block[idx].xpath('a/img/@data-original').get()
            item_loop['jump_url'] = post_block[idx].xpath('span/a/@href').get()
            item_loop['title'] = post_block[idx].xpath('span/a/text()').get()
            item_loop['day'] = post_block[idx].xpath('span[@class="time"]/text()').get()
            yield item_loop
            print('item_loop: %s' % item_loop)
            if item['jump_url']:
                print(item['jump_url'])
                yield scrapy.Request(item['jump_url'], callback=self.parse_detail)

        next_page = response.xpath('//div[@class="pagination"]/div/a[@class="next page-numbers"]/@href').get()
        print('next_page :%s' % next_page)
        if next_page:
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_detail(self, response):
        item_detail = MzituItem()

        item_detail['url'] = response.url
        item_detail['title'] = response.xpath('//div[@class="content"]/h2[@class="main-title"]/text()').get()
        item_detail['category'] = response.xpath('//div[@class="currentpath"]/a[@rel="category tag"]/text()').get()
        item_detail['category_link'] = response.xpath('//div[@class="currentpath"]/a[@rel="category tag"]/@href').get()
        item_detail['publish_time'] = re.search('发布于 (.*?) (.*?)', response.xpath('//div[@class="main-meta"]/span/text()')[1].get()).group(1)
        item_detail['tags'] = response.xpath('//div[@class="main-tags"]/a[@rel="tag"]/text()').getall()
        item_detail['tags_link'] = response.xpath('//div[@class="main-tags"]/a[@rel="tag"]/@href').getall()
        fig_size = int(response.xpath('//div[@class="pagenavi"]/a')[-2].xpath('span/text()').get())

        item_detail['large_pics'] = [yield scrapy.Request(response.url+'/'+str(idx+1), callback=fetch_figure) for idx in range(fig_size)]
        yield item_detail


def fetch_figure(self, response):
    current_fig = response.xpath('//div[@class="main-image"]/p/a/img/@src').get()
    return current_fig
