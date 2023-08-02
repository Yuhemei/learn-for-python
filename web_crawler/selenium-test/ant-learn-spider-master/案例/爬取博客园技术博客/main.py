url = "https://www.cnblogs.com/AggSite/AggSitePostList"
import requests
import json

from bs4 import BeautifulSoup

headers = {
  "content-type": "application/json; charset=UTF-8",
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
}


def craw_page(page_index):
  data = {"CategoryType": "SiteHome",
          "ParentCategoryId": 0,
          "CategoryId": 808,
          "PageIndex": page_index,
          "TotalPostCount": 4000,
          "ItemListActionName": "AggSitePostList"}
  resp = requests.post(url, json.dumps(data), headers=headers)
  return resp.text


def parse_data(html):
  soup = BeautifulSoup(html, "html.parser")
  articles = soup.find_all("article", class_="post-item")
  datas = []
  for article in articles:
    link = article.find("a", class_="post-item-title")
    title = link.get_text()
    href = link["href"]

    author = article.find("a", class_="post-item-author").get_text()

    icon_digg = 0
    icon_comment = 0
    icon_views = 0
    for a in article.find_all("a"):
      if "icon_digg" in str(a):
        icon_digg = a.find("span").get_text()
      if "icon_comment" in str(a):
        icon_comment = a.find("span").get_text()
      if "icon_views" in str(a):
        icon_views = a.find("span").get_text()

    datas.append([title, href, author, icon_digg, icon_comment, icon_views])
  return datas


all_datas = []
for page in range(200):
  print("正在爬取：", page)
  html = craw_page(page)
  datas = parse_data(html)
  all_datas.extend(datas)

import pandas as pd

df = pd.DataFrame(all_datas, columns=["title", "href", "author", "icon_digg", "icon_comment", "icon_views"])
df.to_excel("博客园200页文章信息.xlsx", index=False)

