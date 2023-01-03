# 쿠팡 웹스크래핑 금지? (봇활용한 스크래핑 금지된 것으로 보임)

import requests
from bs4 import BeautifulSoup


print("시작")

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
print("이게 오래 걸리나?")
data = requests.get('https://www.coupang.com/vp/products/1831995302?itemId=3115972008&vendorItemId=71238153782&q=%EA%B5%B0%EA%B3%A0%EA%B5%AC%EB%A7%88+%EA%B8%B0%EA%B3%84&itemsCount=36&searchId=bcb57c7d1e8f41cb8a3efa3a22c38d8d&rank=9&isAddedCart=',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')


print("중간")
title = soup.select_one("#contents > div.prod-atf > div > div.prod-buy.new-oos-style.not-loyalty-member.eligible-address.without-subscribe-buy-type.DISPLAY_0.only-one-delivery.with-seller-store-rating > div.prod-buy-header > h2")
image = soup.select_one("#repImageContainer > img")
price = soup.select_one("#contents > div.prod-atf > div > div.prod-buy.new-oos-style.not-loyalty-member.eligible-address.without-subscribe-buy-type.DISPLAY_0.only-one-delivery.with-seller-store-rating > div.prod-price-container > div.prod-price > div > div.prod-sale-price.prod-major-price > span.total-price > strong")
print("끝")

print('title : ', title.text)
print('image : ', image['src'])
print('price : ', price.text)

# print(soup)  # HTML을 받아온 것을 확인할 수 있다.