'''
Author: hemei yuhemei8088@163.com
Date: 2023-07-31 15:38:16
LastEditors: hemei yuhemei8088@163.com
LastEditTime: 2023-07-31 15:53:40
FilePath: /web_crawler/utils/url_manager.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''


class UrlManager():

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None or len(url) == 0:
            return
        if url in self.new_urls or url in self.old_urls:
            return
        self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def get_new_url(self):
        if self.has_new_url():
            url = self.new_urls.pop()
            self.old_urls.add(url)
            return url
        else:
            return None

    def has_new_url(self):
        return len(self.new_urls) > 0


if __name__ == "__main__":
    url_manager = UrlManager()
    url_manager.add_new_url("http://www.baidu.com")
    url_manager.add_new_url("http://www.baidu.com")
    url_manager.add_new_url("http://www.baidu.com")
    url_manager.get_new_url()
    print(url_manager.new_urls)
    print(url_manager.old_urls)
