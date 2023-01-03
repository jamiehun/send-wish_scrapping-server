from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

DRIVER_PATH = "/chromedriver"
options = Options()
options.headless = True
mobile_emulation = { "deviceName": "iPhone X" }
options.add_experimental_option("mobileEmulation", mobile_emulation)
browser = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

url = "https://www.kurly.com/goods/5065323"
browser.get(url)

#name = browser.find_element(By.CSS_SELECTOR, 'h1').text # CSS_SELECTOR로 가능 
name = browser.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div[1]/div[2]/div[1]/div[2]/h2').text
price = browser.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div[1]/div[2]/div[2]/span[1]').text
img = browser.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div[1]/div[1]/img') # 이미지 스크린샷
img.screenshot("./kurly.png")

print("상품 이름 : ", name)
print("가격 : ", price)
print("상품 이미지 : ", img)

browser.quit()