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