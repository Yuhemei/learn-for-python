import time

import pandas as pd
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = Chrome()

df = pd.read_excel("student_grades.xlsx")

# {'姓名': '馨苒', '语文成绩': 63, '数学成绩': 70, '英语成绩': 86}
for idx, row in df.iterrows():
    driver.get("http://antpython.net/webspider/grade_form")
    WebDriverWait(driver, 5).until(lambda d: "已提交数据" in d.page_source)
    姓名 = row["姓名"]
    语文成绩 = row["语文成绩"]
    数学成绩 = row["数学成绩"]
    英语成绩 = row["英语成绩"]
    driver.find_element(By.XPATH, '//*[@id="sname"]').send_keys(姓名)
    time.sleep(0.2)
    driver.find_element(By.XPATH, '//*[@id="yuwen"]').send_keys(语文成绩)
    time.sleep(0.2)
    driver.find_element(By.XPATH, '//*[@id="shxue"]').send_keys(数学成绩)
    time.sleep(0.2)
    driver.find_element(By.XPATH, '//*[@id="yingyu"]').send_keys(英语成绩)
    time.sleep(0.2)
    driver.find_element(By.XPATH,
                        '//*[@id="submit_button"]').click()
    WebDriverWait(driver, 5).until(
        lambda d: "提交成功！" in d.page_source)

driver.close()
