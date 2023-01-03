import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://shopping.naver.com/window-products/brandfashion/7534550380?NaPm=ct%3Dlcesh5l5%7Cci%3Dshoppingwindow%7Ctr%3Dswl%7Chk%3D08ec8c148ceefbb8dfc93537dc35f2a82e79d26a%7Ctrx%3D',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

title = soup.select_one("#content > div._2-I30XS1lA > div._2QCa6wHHPy > fieldset > div._3k440DUKzy > div._1eddO7u4UC > h3")
image = soup.select_one("#content > div._2-I30XS1lA > div._25tOXGEYJa._2v2w48lRc_ > div._38rEjARje3 > div._23RpOU6xpc._2KRGoy-HE2 > img")
price = soup.select_one("#content > div._2-I30XS1lA > div._2QCa6wHHPy > fieldset > div._3k440DUKzy > div.WrkQhIlUY0 > div > strong > span._1LY7DqCnwR")

print('title : ', title.text)
print('image : ', image['src'])
print('price : ', price.text)