import scrapy
from bs4 import BeautifulSoup

from scrapy_cnblogs.items import ScrapyCnblogsItem


class CnblogsSpider(scrapy.Spider):
    name = 'cnblogs'

    allowed_domains = ['cnblogs.com']

    start_urls = [f"https://www.cnblogs.com/#p{idx}"
                  for idx in range(1, 200 + 1)]

    def parse(self, response: scrapy.http.Response):
        soup = BeautifulSoup(response.text, 'html.parser')

        post_items = soup.find_all("article", class_="post-item")
        for post_item in post_items:
            item = ScrapyCnblogsItem()
            item["url"] = post_item.find("a", class_="post-item-title")["href"]
            item["title"] = post_item.find("a", class_="post-item-title").get_text()
            item["author"] = post_item.find("a", class_="post-item-author").get_text()
            item["datetime"] = post_item.find("span", class_="post-meta-item").get_text()
            like, comment, view = post_item.find_all("a", class_="post-meta-item btn")
            item["like_count"] = like.find("span").get_text()
            item["comment_count"] = comment.find("span").get_text()
            item["view_count"] = view.find("span").get_text()

            yield item
