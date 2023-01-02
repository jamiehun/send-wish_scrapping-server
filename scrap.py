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



driver.get("https://www.musinsa.com/app/goods/2751768/0")
# print(driver.page_source)
# 테스트케이스 1 : https://www.musinsa.com/app/goods/2946394?loc=goods_rank : 성공
# 테스트케이스 2 : https://www.musinsa.com/app/goods/2912231 : 성공
# 테스트케이스 3 : https://www.musinsa.com/app/goods/2288426 : 성공
# 테스트케이스 4 : https://www.musinsa.com/app/goods/1937359 : 성공
# 테스트케이스 5 : https://www.musinsa.com/app/goods/2751768/0 : 


# 상품 정보
search_box_product = driver.find_element(By.XPATH,'//*[@id="page_product_detail"]/div[3]/div[3]/span/em')
print("상품정보 : ", search_box_product.text)

# 상품 이미지 정보
search_box_image = driver.find_element(By.XPATH,'//*[@id="bigimg"]')
print("상품이미지정보 : ", search_box_image.get_attribute('src'))

# 가격정보 (최초가)
search_box_initial_price = driver.find_element(By.XPATH,'//*[@id="goods_price"]/del')
print("최초가격 : ", search_box_initial_price.text)

# 가격정보 (회원가)
search_box_member_price_btn = driver.find_element(By.XPATH, '//*[@id="list_price"]/i')
search_box_member_price_btn.click()

search_box_member = driver.find_element(By.CLASS_NAME, 'member_price')
search_box_member_info = search_box_member.find_elements(By.TAG_NAME, 'li')

for info in search_box_member_info:
    # member_info = info.find_elements(By.TAG_NAME, 'li')
    grade = info.text
    print(grade)

        

# 비회원  
# 뉴비 : //*[@id="sPrice"]/ul/li[2]/span[2]
# 루키
# 멤버
# 브론즈
# 실버
# 골드
# 플래티넘
# 다이아몬드 : //*[@id="sPrice"]/ul/li[9]/span[2]


driver.quit()