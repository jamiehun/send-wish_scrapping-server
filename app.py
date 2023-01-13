from flask import Flask, request
from selenium_main import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello sendwish web scrapper!'

@app.route('/webscrap', methods=['POST'])
def webscrap():
    data = request.get_json()
    url_receive = data['url'][0]
    # [todo] 예외처리 필요
    print("===before enter")
    result = run(url_receive)
    return result

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)