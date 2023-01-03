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
mobile_emulation = { "deviceName": "iPhone X" }
options.add_experimental_option("mobileEmulation", mobile_emulation)


chrome_driver = ChromeDriverManager().install()
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

# 쿠팡
driver.get("https://m.coupang.com/vm/products/6552462584?itemId=14634004658&vendorItemId=81875544125")
# 네이버
# driver.get("https://m.shopping.naver.com/kids/stores/1000016176/products/4847841465?NaPm=ct%3Dlcfs8ykw%7Cci%3D6ae6545058bf0a5b6906fdb0e42605ec5ab66f78%7Ctr%3Dbrc%7Csn%3D203038%7Chk%3Dafd41c17626461775eeac008bf5481009bea4150")
# 무신사

# 모바일 환경 닫기 (추후 예외처리)
close_btn = driver.find_element(By.XPATH, '//*[@id="fullBanner"]/div/div/a[2]')
close_btn.click()

get_url = driver.current_url

# ID 뜰 때까지 대기 (추후 예외처리)
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pdpImages"]/ul/li[1]/img')))

## xpath 활용하지 않고 들고오기 (쿠팡)
# 1. 이미지
# 2. 상품명
# 3. 상품가격
# 4. 할인가격 
img_collector = driver.find_element(By.ID, "pdpImages")
imgs = img_collector.find_elements(By.TAG_NAME, 'img')
for i in imgs:
    img = i.get_attribute("src")
    # print(img)
    if 136 < img.__sizeof__()<= 400:
        print("이미지: ", img)
        break
    

# print("이미지: ", img)

# print("할인가: ", discount_price.text)

driver.quit()

