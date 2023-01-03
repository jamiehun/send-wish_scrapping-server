# 크롬 브라우저 기준
import selenium
from selenium import webdriver
# from selenium.webdriver import ActionChains

# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

# https://sites.google.com/chromium.org/driver/?pli=1
DRIVER_PATH = '/chromedriver'

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)



driver.get("https://www.seoulstore.com/products/1522613/detail")


imgs = driver.find_elements(By.TAG_NAME, 'img')
for i in imgs:
    img = i.get_attribute("src")
    if img:
        print(img)


driver.quit()