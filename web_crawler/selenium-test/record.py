from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = Chrome()  # Optional argument, if not specified will search path.

driver.get('https://www.python.org/');

WebDriverWait(driver, 10).until(lambda d: "Python" in d.title)

textElement = driver.find_element(By.XPATH, '//*[@id="touchnav-wrapper"]/header/div/div[3]/p' )
print(driver.current_url)
print(driver.title)
print(driver.maximize_window())
print(driver.fullscreen_window())
driver.save_screenshot("./images/image.png")
textElement.screenshot("./images/text.png")
# driver.close()