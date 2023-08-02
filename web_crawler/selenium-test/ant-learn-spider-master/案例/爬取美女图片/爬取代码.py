"""
爬取图片，并且下载图片
url:https://pic.netbian.com/4kmeinv/

爬取网页requests
解析网页beautifulsoup

"""

# 获取网页的源代码
# url = "https://pic.netbian.com/4kmeinv/"
# url = "https://pic.netbian.com/4kmeinv/index_3.html"

import requests
from bs4 import BeautifulSoup
import os

def craw_html(url):
  resp = requests.get(url)
  resp.encoding='gbk'
  print(resp.status_code)
  print(resp.text)
  html = resp.text
  # print(html)
  return html

def parse_and_download(html):
  # 解析图片的地址
  soup = BeautifulSoup(html, "html.parser")
  imgs = soup.find_all("img")
  for img in imgs:
    src = img["src"]
    if "/uploads/" not in src:
      continue
    src = f"https://pic.netbian.com{src}"
    print(src)

    # 首先得到图片的本地文件地址
    filename = os.path.basename(src)
    with open(f"美女图片/{filename}", "wb") as f:
      resp_img = requests.get(src)
      f.write(resp_img.content)

urls = ["https://pic.netbian.com/4kmeinv/"] + [
  f"https://pic.netbian.com/4kmeinv/index_{i}.html"
  for i in range(2, 11)
]
for url in urls:
  print("#### 正在爬取:", url)
  html = craw_html(url)
  parse_and_download(html)