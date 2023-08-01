import time
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = Chrome()  # Optional argument, if not specified will search path.

driver.get('https://www.baidu.com/')

driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys("python")
driver.find_element(By.XPATH,'//*[@id="su"]').click()
time.sleep(10000)
# driver.close()
