import json
from flask import Flask, request
from categorization import categorization
from categorization import categorization

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello sendwish ai server!'

@app.route('/category', methods=['POST'])
def category():
    data = request.get_json()
    # img_url = data['img_url'][0]
    # {'imgUrl':'https://image.msscdn.net/images/prd_img/20110902/12345/detail_12345_1_960.jpg?t=20220628094033'}
    print("===========================")
    print(data)
    img_url = data['imgUrl']
    print("img_url", img_url)
    # [todo] 예외처리 필요
    print("===Start Categorization===")
    return categorization(img_url)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)

# 실행 명령어
# gunicorn app:app -b 0.0.0.0:5000 -w 2 --timeout=360 -k gevent 