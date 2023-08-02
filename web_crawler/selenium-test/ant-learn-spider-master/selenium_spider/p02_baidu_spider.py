import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import title_contains

driver = Chrome()
driver.get("https://www.baidu.com/")

driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("python")
driver.find_element(By.XPATH, '//*[@id="su"]').click()

WebDriverWait(driver, 60).until(title_contains("python"))

while True:
  h3_list = driver.find_elements(By.CSS_SELECTOR, 'h3.t')
  for h3 in h3_list:
    print(h3.text)

  driver.find_element(By.XPATH, '//*[@id="page"]/div/a[last()]').click()
  time.sleep(3)

