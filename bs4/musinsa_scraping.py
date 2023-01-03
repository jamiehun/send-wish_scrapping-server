import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.musinsa.com/app/goods/2875755?loc=goods_rank',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

title = soup.select_one("#page_product_detail > div.right_area.page_detail_product > div.right_contents.section_product_summary > span > em")
image = soup.select_one("#bigimg")

try:
    if(image['src'].find("https:")) == -1:
        image = "https:" + image['src'] 
finally:
    print("=== !!!파싱 정보 확인 필요 : 동적 이미지일시 앞에 https: 생략되어 있음 !!! ===")

price = soup.select_one("#goods_price > del")

print('title : ', title.text)
print('image : ', image)
print('price : ', price.text)
