# 크롬 브라우저 기준
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


# https://sites.google.com/chromium.org/driver/?pli=1
DRIVER_PATH = '/chromedriver'

options = Options()
options = webdriver.ChromeOptions()

# 쿠팡 헤드리스 사용 불가 (막아놓은듯)
# options.add_argument('headless')

options.add_argument("--window-size=1920,1200")
options.add_argument('User-Agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1')
options.add_argument('Accept-Language=ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7')
options.add_argument("lang=ko_KR")

chrome_driver = ChromeDriverManager().install()
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

driver.get("https://m.coupang.com/vm/products/6552462584?itemId=14634004658&vendorItemId=81875544125")

# 모바일 환경 닫기 
close_btn = driver.find_element(By.XPATH, '//*[@id="fullBanner"]/div/div/a[2]')
close_btn.click()

get_url = driver.current_url

# ID 뜰 때까지 대기
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pdpImages"]/ul/li[1]/img')))


# 1. XPATH를 사용하지 않고 바로 들고오기
# title
title_list = driver.find_elements(By.CLASS_NAME, "title")
print("title_list: ", title_list)

# prod-price // prod-price__original // prod-price__sale non-member // prod-price__coupon
price_list = driver.find_elements(By.CLASS_NAME, "prod-price")
print("price_list: ", price_list)


# 2. beautiful soup를 사용해서 들고오기 


print("제목: ", title.text)
print("이미지: ", image.get_attribute("src"))
print("가격: ", price.text)
# print("할인가: ", discount_price.text)

driver.quit()

