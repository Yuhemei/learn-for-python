'''
Author: hemei yuhemei8088@163.com
Date: 2023-07-31 14:51:58
LastEditors: hemei yuhemei8088@163.com
LastEditTime: 2023-07-31 16:53:02
FilePath: /web_crawler/run.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from bs4 import BeautifulSoup
import re

with open("./test.html") as fin:
    html_doc = fin.read()

soup = BeautifulSoup(html_doc, "html.parser")
links = soup.find_all("a")
pattern = r"^http://.*\.com$"
for item in links:
    if re.match(pattern,item["href"]):
        print(item.name, item["href"], item.get_text())
