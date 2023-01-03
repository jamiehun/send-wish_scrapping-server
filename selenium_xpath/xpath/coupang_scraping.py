# 크롬 브라우저 기준
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select


# https://sites.google.com/chromium.org/driver/?pli=1
DRIVER_PATH = '/chromedriver'

options = Options()
options = webdriver.ChromeOptions()
# options.add_argument('headless') # 헤드리스 사용하면 제대로 작동을 안함 
options.add_argument("--window-size=1920,1200")
options.add_argument('User-Agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1')
options.add_argument('Accept-Language=ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7')
options.add_argument("lang=ko_KR")

chrome_driver = ChromeDriverManager().install()
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """})

driver.get("https://m.coupang.com/vm/products/6552462584?itemId=14634004658&vendorItemId=81875544125")

close_btn = driver.find_element(By.XPATH, '//*[@id="fullBanner"]/div/div/a[2]')
close_btn.click()

get_url = driver.current_url

# print(get_url)

# ID에 따라서 대기하도록 하기 
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pdpImages"]/ul/li[1]/img')))

# 0. (기본)XPATH로 해당 명령어 들고 오기
title = driver.find_element(By.XPATH,'//*[@id="product-info"]/dt') # 상품 제목
image = driver.find_element(By.XPATH,'//*[@id="pdpImages"]/ul/li[1]/img') # 상품 이미지 
price = driver.find_element(By.XPATH,'//*[@id="productPriceArea"]/div[1]/dl/dd[3]/span') # 상품 가격 
# discount_price = driver.find_element(By.XPATH,'//*[@id="contents"]/div[1]/div/div[3]/div[5]/div[1]/div/div[3]/span[1]/strong') # 상품 할인 가격 

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

